import streamlit as st
import time
from utils import (
    check_password,
    check_if_interview_completed,
    save_interview_data,
)
import os
import config


# --- Extract Prolific PID from URL ---
query_params = st.query_params()
prolific_pid = query_params.get("PROLIFIC_PID", [None])[0]
if prolific_pid:
    st.markdown(f"👤 Participant ID: `{prolific_pid}`")

# --- Load API library ---
if "gpt" in config.MODEL.lower():
    api = "openai"
    from openai import OpenAI
elif "claude" in config.MODEL.lower():
    api = "anthropic"
    import anthropic
else:
    raise ValueError("Model does not contain 'gpt' or 'claude'; unable to determine API.")

# --- Set Streamlit UI ---
st.set_page_config(page_title="NIM Interview", page_icon=config.AVATAR_INTERVIEWER)

# --- Determine user identity ---
if config.LOGINS:
    pwd_correct, username = check_password()
    if not pwd_correct:
        st.stop()
    else:
        st.session_state.username = username
else:
    st.session_state.username = prolific_pid or "testaccount"

# --- Ensure output folders exist ---
for folder in [config.TRANSCRIPTS_DIRECTORY, config.TIMES_DIRECTORY, config.BACKUPS_DIRECTORY]:
    os.makedirs(folder, exist_ok=True)

# --- Initialise session state ---
st.session_state.setdefault("interview_active", True)
st.session_state.setdefault("messages", [])
if "start_time" not in st.session_state:
    st.session_state.start_time = time.time()
    st.session_state.start_time_file_names = time.strftime(
        "%Y_%m_%d_%H_%M_%S", time.localtime(st.session_state.start_time)
    )

# --- Check for previous completion ---
interview_previously_completed = check_if_interview_completed(
    config.TIMES_DIRECTORY, st.session_state.username
)
if interview_previously_completed and not st.session_state.messages:
    st.session_state.interview_active = False
    st.markdown("Interview already completed.")

# --- Quit Button ---
col1, col2 = st.columns([0.85, 0.15])
with col2:
    if st.session_state.interview_active and st.button("Quit", help="End the interview."):
        st.session_state.interview_active = False
        quit_message = "You have cancelled the interview."
        st.session_state.messages.append({"role": "assistant", "content": quit_message})
        save_interview_data(
            st.session_state.username,
            config.TRANSCRIPTS_DIRECTORY,
            config.TIMES_DIRECTORY,
        )

# --- Display Previous Messages ---
for message in st.session_state.messages[1:]:
    if not any(code in message["content"] for code in config.CLOSING_MESSAGES.keys()):
        avatar = config.AVATAR_INTERVIEWER if message["role"] == "assistant" else config.AVATAR_RESPONDENT
        with st.chat_message(message["role"], avatar=avatar):
            st.markdown(message["content"])

# --- Load API Client ---
if api == "openai":
    client = OpenAI(api_key=st.secrets["API_KEY_OPENAI"])
    api_kwargs = {"stream": True}
elif api == "anthropic":
    client = anthropic.Anthropic(api_key=st.secrets["API_KEY_ANTHROPIC"])
    api_kwargs = {"system": config.SYSTEM_PROMPT}

api_kwargs.update({
    "messages": st.session_state.messages,
    "model": config.MODEL,
    "max_tokens": config.MAX_OUTPUT_TOKENS,
})
if config.TEMPERATURE is not None:
    api_kwargs["temperature"] = config.TEMPERATURE

# --- If no prior conversation, start interview ---
if not st.session_state.messages:
    if api == "openai":
        st.session_state.messages.append({"role": "system", "content": config.SYSTEM_PROMPT})
        with st.chat_message("assistant", avatar=config.AVATAR_INTERVIEWER):
            stream = client.chat.completions.create(**api_kwargs)
            message_interviewer = st.write_stream(stream)
    elif api == "anthropic":
        st.session_state.messages.append({"role": "user", "content": "Hi"})
        with st.chat_message("assistant", avatar=config.AVATAR_INTERVIEWER):
            message_placeholder = st.empty()
            message_interviewer = ""
            with client.messages.stream(**api_kwargs) as stream:
                for delta in stream.text_stream:
                    if delta:
                        message_interviewer += delta
                    message_placeholder.markdown(message_interviewer + "▌")
            message_placeholder.markdown(message_interviewer)
    st.session_state.messages.append({"role": "assistant", "content": message_interviewer})

    save_interview_data(
        username=st.session_state.username,
        transcripts_directory=config.BACKUPS_DIRECTORY,
        times_directory=config.BACKUPS_DIRECTORY,
        file_name_addition_transcript=f"_transcript_started_{st.session_state.start_time_file_names}",
        file_name_addition_time=f"_time_started_{st.session_state.start_time_file_names}",
    )

# --- Main Chat Loop ---
if st.session_state.interview_active:
    if user_input := st.chat_input("Your message here"):
        st.session_state.messages.append({"role": "user", "content": user_input})
        with st.chat_message("user", avatar=config.AVATAR_RESPONDENT):
            st.markdown(user_input)

        with st.chat_message("assistant", avatar=config.AVATAR_INTERVIEWER):
            placeholder = st.empty()
            message_interviewer = ""

            if api == "openai":
                stream = client.chat.completions.create(**api_kwargs)
                for msg in stream:
                    delta = msg.choices[0].delta.content
                    if delta:
                        message_interviewer += delta
                    if len(message_interviewer) > 5:
                        placeholder.markdown(message_interviewer + "▌")
                    if any(code in message_interviewer for code in config.CLOSING_MESSAGES.keys()):
                        placeholder.empty()
                        break

            elif api == "anthropic":
                with client.messages.stream(**api_kwargs) as stream:
                    for delta in stream.text_stream:
                        if delta:
                            message_interviewer += delta
                        if len(message_interviewer) > 5:
                            placeholder.markdown(message_interviewer + "▌")
                        if any(code in message_interviewer for code in config.CLOSING_MESSAGES.keys()):
                            placeholder.empty()
                            break

            if not any(code in message_interviewer for code in config.CLOSING_MESSAGES.keys()):
                placeholder.markdown(message_interviewer)
                st.session_state.messages.append({"role": "assistant", "content": message_interviewer})
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

            for code in config.CLOSING_MESSAGES.keys():
                if code in message_interviewer:
                    st.session_state.messages.append({"role": "assistant", "content": message_interviewer})
                    st.session_state.interview_active = False
                    st.markdown(config.CLOSING_MESSAGES[code])
                    st.session_state.messages.append({"role": "assistant", "content": config.CLOSING_MESSAGES[code]})

                    final_transcript_stored = False
                    while not final_transcript_stored:
                        save_interview_data(
                            username=st.session_state.username,
                            transcripts_directory=config.TRANSCRIPTS_DIRECTORY,
                            times_directory=config.TIMES_DIRECTORY,
                        )
                        final_transcript_stored = check_if_interview_completed(
                            config.TRANSCRIPTS_DIRECTORY, st.session_state.username
                        )
                        time.sleep(0.1)

                    # --- Prolific redirect after completion ---
                    COMPLETION_CODE = "CGR8B7PK"  
                    if prolific_pid:
                        redirect_url = f"https://app.prolific.com/submissions/complete?cc=CGR8B7PK"
                        st.markdown(f'<meta http-equiv="refresh" content="3;url={redirect_url}">', unsafe_allow_html=True)
