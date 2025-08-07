import streamlit as st
import time
import os
import json
from openai import OpenAI
from utils import (
    check_password,
    check_if_interview_completed,
    save_interview_data,
)
import config

# Page setup
st.set_page_config(page_title="chatbot", page_icon=config.AVATAR_INTERVIEWER)

# Helper functions (only for reused functionality)
def save_backup_data():
    """Save backup interview data"""
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

def find_closing_code(text):
    """Find closing code in text """
    return next((code for code in config.CLOSING_MESSAGES if code in text), None)

def save_timing_data(event_type, duration, message_index, message_content):
    """Save timing data to a separate log file"""
    timing_entry = {
        "timestamp": time.time(),
        "event_type": event_type,  # "chatbot_response" or "human_response"
        "duration_seconds": duration,
        "message_index": message_index,
        "message_length_chars": len(message_content),
        "message_content": message_content,
        "username": st.session_state.username
    }
    
    # Create timing log file
    timing_file = os.path.join(
        config.TRANSCRIPTS_DIRECTORY, 
        f"{st.session_state.username}_timings.jsonl"
    )
    
    try:
        with open(timing_file, "a", encoding='utf-8') as f:
            f.write(json.dumps(timing_entry, ensure_ascii=False) + "\n")
    except Exception as e:
        # Fallback: save without message content if JSON serialization fails
        try:
            fallback_entry = timing_entry.copy()
            fallback_entry["message_content"] = f"[ENCODING_ERROR: {str(e)}]"
            with open(timing_file, "a", encoding='utf-8') as f:
                f.write(json.dumps(fallback_entry, ensure_ascii=False) + "\n")
        except:
            pass

# Auth + username
if config.LOGINS and True:  # test_Mode assumed True
    pwd_correct, username = check_password()
    if not pwd_correct:
        st.stop()
    st.session_state.username = username

# Create data directories
for directory in [config.TRANSCRIPTS_DIRECTORY, config.TIMES_DIRECTORY, config.BACKUPS_DIRECTORY]:
    os.makedirs(directory, exist_ok=True)

# Initialize session state with defaults
defaults = {
    "interview_active": True,
    "messages": [],
    "start_time": time.time(),
    "closing_code_found": None,
    "startNextPhase": False,
    "initial_message_displayed": False,
    'file_suffix': "_interview",
    "last_assistant_response_start": None,  # Track when assistant starts responding
    "last_user_input_time": None,  # Track when user can start typing
}

for key, value in defaults.items():
    if key not in st.session_state:
        st.session_state[key] = value

# Generate timestamp for file names
if "start_time_file_names" not in st.session_state:
    st.session_state.start_time_file_names = time.strftime(
        "%Y_%m_%d_%H_%M_%S", time.localtime(st.session_state.start_time)
    )

# Check for phase transition
if st.session_state.startNextPhase:
    st.switch_page("pages/demographics.py")

# Setup API client
if "gpt" not in config.MODEL.lower():
    raise ValueError("Unsupported model type.")

client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY", st.secrets["API_KEY_OPENAI"]))
api_kwargs = {
    "stream": True,
    "messages": st.session_state.messages,
    "model": config.MODEL,
    "max_tokens": config.MAX_OUTPUT_TOKENS,
}
if config.TEMPERATURE is not None:
    api_kwargs["temperature"] = config.TEMPERATURE

# Prevent duplicate interviews
if (check_if_interview_completed(config.TIMES_DIRECTORY, st.session_state.username, st.session_state.file_suffix) 
    and not st.session_state.messages):
    st.session_state.interview_active = False
    st.warning("Interview already attempted.")

# Handle initial system message
if not st.session_state.messages:
    st.session_state.messages.append({"role": "system", "content": config.SYSTEM_PROMPT})
    
    # Start timing for first chatbot response
    st.session_state.last_assistant_response_start = time.time()
    
    with st.chat_message("assistant", avatar=config.AVATAR_INTERVIEWER):
        # Show "please wait" message initially
        placeholder = st.empty()
        placeholder.markdown("Please wait while I prepare your interview...")
        
        # Stream the actual response
        stream = client.chat.completions.create(**api_kwargs)
        first_msg = ""
        
        for chunk in stream:
            delta = chunk.choices[0].delta.content
            if delta:
                first_msg += delta
                # Replace placeholder with streaming content once we have some text
                if len(first_msg) > 5:
                    placeholder.markdown(first_msg + "▌")
        
        # Show final message without cursor
        placeholder.markdown(first_msg)
    
    # Calculate and save chatbot response duration
    chatbot_duration = time.time() - st.session_state.last_assistant_response_start
    save_timing_data("chatbot_response", chatbot_duration, len(st.session_state.messages), first_msg)
    
    st.session_state.messages.append({"role": "assistant", "content": first_msg})
    st.session_state.initial_message_displayed = True
    
    # Set time when user can start responding
    st.session_state.last_user_input_time = time.time()
    
    save_backup_data()

# Display previous messages
if st.session_state.interview_active:
    # Skip system message and already-displayed initial message
    messages_to_display = st.session_state.messages[1:]  # Skip system message
    if st.session_state.initial_message_displayed and messages_to_display:
        messages_to_display = messages_to_display[1:]  # Skip initial assistant message
    
    for message in messages_to_display:
        if not find_closing_code(message["content"]):
            avatar = config.AVATAR_INTERVIEWER if message["role"] == "assistant" else config.AVATAR_RESPONDENT
            with st.chat_message(message["role"], avatar=avatar):
                st.markdown(message["content"])

# Chat input + response logic
if st.session_state.interview_active:
    if msg := st.chat_input("Your message here"):
        # Calculate human response duration (time since last chatbot response finished)
        if st.session_state.last_user_input_time:
            human_duration = time.time() - st.session_state.last_user_input_time
            save_timing_data("human_response", human_duration, len(st.session_state.messages), msg)
        
        st.session_state.messages.append({"role": "user", "content": msg})
        
        with st.chat_message("user", avatar=config.AVATAR_RESPONDENT):
            st.markdown(msg)
        
        # Start timing for chatbot response
        st.session_state.last_assistant_response_start = time.time()
        
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
                
                # Check for closing codes during streaming
                if find_closing_code(full_response):
                    break
            
            # Calculate chatbot response duration (streaming complete)
            chatbot_duration = time.time() - st.session_state.last_assistant_response_start
            save_timing_data("chatbot_response", chatbot_duration, len(st.session_state.messages), full_response)
            
            # Determine if interview should close
            closing_code = find_closing_code(full_response)
            elapsed = int(time.time() - st.session_state.start_time)
            if config.TIME_SETTING - elapsed <= 0:
                closing_code = "666_complete_interview"
            
            if closing_code:
                # Handle interview closing
                st.session_state.startNextPhase = True
                st.session_state.closing_code_found = closing_code
                closing_msg = config.CLOSING_MESSAGES[closing_code]
                
                placeholder.empty()
                st.session_state.messages.append({"role": "assistant", "content": full_response})
                st.session_state.messages.append({"role": "assistant", "content": closing_msg})
                st.markdown(closing_msg)
                
                # Save final transcript with retry logic
                final_saved = False
                while not final_saved:
                    save_interview_data(
                        username=st.session_state.username,
                        transcripts_directory=config.TRANSCRIPTS_DIRECTORY,
                        times_directory=config.TIMES_DIRECTORY,
                        file_name_addition_transcript = st.session_state.file_suffix
                    )
                    final_saved = check_if_interview_completed(
                        config.TRANSCRIPTS_DIRECTORY, st.session_state.username, st.session_state.file_suffix,  
                    )
                    time.sleep(0.1)
                st.rerun()
            else:
                # Continue interview - set time when user can start responding
                placeholder.markdown(full_response)
                st.session_state.messages.append({"role": "assistant", "content": full_response})
                st.session_state.last_user_input_time = time.time()
                save_backup_data()