import streamlit as st
import os
from utils import (
    check_password,
    check_if_interview_completed,
    save_interview_data,
)
import config
st.set_page_config(page_title="qOrganizer", page_icon="🧠")
# Auth + username
if config.LOGINS and True:  # test_Mode assumed True
    pwd_correct, username = check_password()
    if not pwd_correct:
        st.stop()
    st.session_state.username = username

st.session_state.selected_q_keys = ["ESS", "IE4", "BFI10"]
st.session_state.numquests = len(st.session_state.selected_q_keys)

# Initialise session state
if "qcount" not in st.session_state:
    st.session_state.qcount = 0
else:
    st.session_state.qcount = st.session_state.qcount + 1

if st.session_state.qcount < st.session_state.numquests:
    st.switch_page("pages/questionnairesForm.py")
else:
    st.switch_page("pages/studyCompleteScreen.py")


