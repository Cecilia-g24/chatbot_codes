# interview.py (landing page)

import streamlit as st
#from streamlit_extras.switch_page_button import switch_page
from utils import (
    check_password,
    check_if_interview_completed,
    save_interview_data,
)
import os
import config

# Test switch (True = test mode with password login, False = Prolific mode)
test_Mode = True

st.set_page_config(page_title="Interview Start", page_icon="💬")


# Extract Prolific parameters from URL 
query_params = st.query_params
prolific_pid = query_params.get("PROLIFIC_PID", [None])
study_id = query_params.get("STUDY_ID", [None])
session_id = query_params.get("SESSION_ID", [None])

# on-screen display to show prolific id
if prolific_pid:
    st.markdown(f"👤 Prolific PID: `{prolific_pid}`")

# Check if usernames and config.logins (always True) and Prolific_mode are enabled
if config.LOGINS and test_Mode:
    pwd_correct, username = check_password()
    if not pwd_correct:
        st.stop()
    else:
        st.session_state.username = username
# set prolific_pid = username, when login function is disabled
else:
    st.session_state.username = prolific_pid or "testaccount"


st.title("Welcome to the AI!!! Interview")
st.write("Thank you for participating in our study. Please click the button below to begin your interview.")

if st.button("▶️ Start Interview"):
    st.switch_page("pages/chatbot.py")
