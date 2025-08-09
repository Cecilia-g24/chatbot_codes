import streamlit as st
import config
import os
import time
from utils import (
    check_password,
    check_prolific_access
)

st.set_page_config(page_title="Completion", page_icon="✅")

# Check if login mode is enabled otherwise prolific mode is assumed
if config.LOGINS:
    pwd_correct, username = check_password()
    if not pwd_correct:
        st.stop()
    else:
        st.session_state.username = username
# set prolific_pid = username, when login function is disabled
else:
    check_prolific_access()


# Record finish time when completion page is loaded
if 'finish_time' not in st.session_state:
    st.session_state.finish_time = time.time()

st.title("🎉 Study Complete")
st.success("You have completed the study. Thank you very much for your time and effort! Please return to Prolific by pressing the button below to log your study completion.")

# Optional comments section
st.markdown("---")
st.subheader("📝 Optional Feedback")
st.write("If you have any comments or remarks about the study, please feel free to share them below (optional):")

comments = st.text_area(
    "Your comments:",
    placeholder="Any thoughts, suggestions, or feedback about your experience with this study...",
    height=100,
    label_visibility="collapsed"
)

st.markdown("---")

if st.button("Return to Prolific"):
    # Save completion data (timing + optional comments)
    username = st.session_state.get('username', 'anonymous_user')
    comments_directory = config.TRANSCRIPTS_DIRECTORY 
    
    # Create directory if it doesn't exist
    os.makedirs(comments_directory, exist_ok=True)
    
    comments_file_path = os.path.join(comments_directory, f"{username}_completion.txt")
    
    # Calculate study duration
    start_time = st.session_state.get('start_time', st.session_state.finish_time)
    duration_minutes = (st.session_state.finish_time - start_time) / 60
    
    with open(comments_file_path, "w", encoding="utf-8") as f:
        f.write(f"Study Completion Data\n")
        f.write(f"Username: {username}\n")
        f.write(f"Start time (UTC): {time.strftime('%d/%m/%Y %H:%M:%S', time.localtime(start_time))}\n")
        f.write(f"Finish time (UTC): {time.strftime('%d/%m/%Y %H:%M:%S', time.localtime(st.session_state.finish_time))}\n")
        f.write(f"Study duration (minutes): {duration_minutes:.2f}\n")
        f.write(f"Comments: {comments if comments.strip() else 'No comments provided'}\n")
    
    st.markdown(
        f'<meta http-equiv="refresh" content="0; url={config.prolific_completion_url}">',
        unsafe_allow_html=True,
    )