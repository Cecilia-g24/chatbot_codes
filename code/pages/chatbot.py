import streamlit as st
import time
import os
from openai import OpenAI
from utils import (
    check_password,
    check_if_interview_completed,
    save_interview_data,
)
import config

# Page setup
st.set_page_config(page_title="chatbot", page_icon=config.AVATAR_INTERVIEWER)

# Auth + username
if config.LOGINS and True:  # test_Mode assumed True
    pwd_correct, username = check_password()
    if not pwd_correct:
        st.stop()
    st.session_state.username = username


# Create data directories
os.makedirs(config.TRANSCRIPTS_DIRECTORY, exist_ok=True)
os.makedirs(config.TIMES_DIRECTORY, exist_ok=True)
os.makedirs(config.BACKUPS_DIRECTORY, exist_ok=True)

# Initialise session state
if "interview_active" not in st.session_state:
    st.session_state.interview_active = True

# Initialise messages list in session state
if "messages" not in st.session_state:
    st.session_state.messages = []

# Store start time in session state
if "start_time" not in st.session_state:
    st.session_state.start_time = time.time()
    st.session_state.start_time_file_names = time.strftime(
        "%Y_%m_%d_%H_%M_%S", time.localtime(st.session_state.start_time)
    )
# Initialize closing code for ending interview
if "closing_code_found" not in st.session_state:
    st.session_state.closing_code_found = None
if "startNextPhase" not in st.session_state:
    st.session_state.startNextPhase = False

if st.session_state.startNextPhase == True:
    st.switch_page("pages/demographics.py")
    
# Load API client
if "gpt" in config.MODEL.lower():
    client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY", st.secrets["API_KEY_OPENAI"]))
    api_kwargs = {
        "stream": True,
        "messages": st.session_state.messages,
        "model": config.MODEL,
        "max_tokens": config.MAX_OUTPUT_TOKENS,
    }
    if config.TEMPERATURE is not None:
        api_kwargs["temperature"] = config.TEMPERATURE
else:
    raise ValueError("Unsupported model type.")

# Prevent duplicate interviews
if check_if_interview_completed(config.TIMES_DIRECTORY, st.session_state.username) and not st.session_state.messages:
    st.session_state.interview_active = False
    st.warning("Interview already attempted.")

# Initial system prompt
if not st.session_state.messages:
    st.session_state.messages.append({"role": "system", "content": config.SYSTEM_PROMPT})
    with st.chat_message("assistant", avatar=config.AVATAR_INTERVIEWER):
        stream = client.chat.completions.create(**api_kwargs)
        first_msg = st.write_stream(stream)
    st.session_state.messages.append({"role": "assistant", "content": first_msg})
    save_interview_data(
        username=st.session_state.username,
        transcripts_directory=config.BACKUPS_DIRECTORY,
        times_directory=config.BACKUPS_DIRECTORY,
        file_name_addition_transcript=f"_transcript_started_{st.session_state.start_time_file_names}",
        file_name_addition_time=f"_time_started_{st.session_state.start_time_file_names}",
    )

# Display previous messages
if st.session_state.interview_active:
    # Skip the first assistant message if we just displayed it during initialization
    start_index = 2 if len(st.session_state.messages) > 1 and st.session_state.messages[1]["role"] == "assistant" else 1
    for message in st.session_state.messages[start_index:]:
        if not any(code in message["content"] for code in config.CLOSING_MESSAGES.keys()):
            avatar = config.AVATAR_INTERVIEWER if message["role"] == "assistant" else config.AVATAR_RESPONDENT
            with st.chat_message(message["role"], avatar=avatar):
                st.markdown(message["content"])

# Chat input + response logic
if st.session_state.interview_active:
    if msg := st.chat_input("Your message here"):
        st.session_state.messages.append({"role": "user", "content": msg})
        with st.chat_message("user", avatar=config.AVATAR_RESPONDENT):
            st.markdown(msg)

        with st.chat_message("assistant", avatar=config.AVATAR_INTERVIEWER):
            placeholder = st.empty()
            full_response = ""
            stream = client.chat.completions.create(**api_kwargs)
            for chunk in stream:
                delta = chunk.choices[0].delta.content
                if delta:
                    full_response += delta
                    if len(full_response) > 5:
                        placeholder.markdown(full_response + "▌")
                if any(code in full_response for code in config.CLOSING_MESSAGES):
                    break

            closing_code = next((code for code in config.CLOSING_MESSAGES if code in full_response), None)
            elapsed = int(time.time() - st.session_state.start_time)
            if config.TIME_SETTING - elapsed <= 0:
                closing_code = "666_complete_interview"

            if closing_code:
                st.session_state.startNextPhase = True
                #st.session_state.interview_active = False
                st.session_state.closing_code_found = closing_code
                closing_msg = config.CLOSING_MESSAGES[closing_code]
                placeholder.empty()
                st.session_state.messages.append({"role": "assistant", "content": full_response})
                st.session_state.messages.append({"role": "assistant", "content": closing_msg})
                st.markdown(closing_msg)

                # Save final transcript
                final_saved = False
                while not final_saved:
                    save_interview_data(
                        username=st.session_state.username,
                        transcripts_directory=config.TRANSCRIPTS_DIRECTORY,
                        times_directory=config.TIMES_DIRECTORY,
                    )
                    final_saved = check_if_interview_completed(
                        config.TRANSCRIPTS_DIRECTORY, st.session_state.username
                    )
                    time.sleep(0.1)
            else:
                placeholder.markdown(full_response)
                st.session_state.messages.append({"role": "assistant", "content": full_response})
                try:
                    save_interview_data(
                        username=st.session_state.username,
                        transcripts_directory=config.BACKUPS_DIRECTORY,
                        times_directory=config.BACKUPS_DIRECTORY,
                        file_name_addition_transcript=f"_transcript_started_{st.session_state.start_time_file_names}",
                        file_name_addition_time=f"_time_started_{st.session_state.start_time_file_names}",
                    )
                except:
                    pass
