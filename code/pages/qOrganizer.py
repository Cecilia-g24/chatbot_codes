import streamlit as st
import os
from utils import (
    check_password,
    check_if_interview_completed,
    save_interview_data,
)
import config
st.set_page_config(page_title="questionnaires", page_icon="🧠")
# Auth + username
if config.LOGINS and True:  # test_Mode assumed True
    pwd_correct, username = check_password()
    if not pwd_correct:
        st.stop()
    st.session_state.username = username


# Initialise session state
if "next_q" not in st.session_state:
    st.session_state.next_q = 0
else:
    st.session_state.next_q = st.session_state.next_q + 1

if st.session_state.next_q <= 7:
    st.switch_page("pages/questionnairesForm.py")
else:
    st.switch_page("pages/studyCompleteScreen.py")


