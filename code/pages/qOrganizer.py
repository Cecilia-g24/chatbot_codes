import streamlit as st
import os
import random
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

# Initialize the questionnaire list - randomize only on first run
if "selected_q_keys" not in st.session_state:
    # First time running - create randomized order
    questionnaire_list = ["ESS", "ATAS", "ASKU", "IE4", "L1", "BFI10", "ICTSC25"]
    random.shuffle(questionnaire_list)
    st.session_state.selected_q_keys = questionnaire_list
    st.session_state.numquests = len(st.session_state.selected_q_keys)
else:
    # Already exists in session_state - use the existing randomized order
    pass

# Initialize session state
if "qcount" not in st.session_state:
    st.session_state.qcount = 0
else:
    st.session_state.qcount = st.session_state.qcount + 1

if st.session_state.qcount < st.session_state.numquests:
    st.switch_page("pages/questionnairesForm.py")
else:
    st.switch_page("pages/studyCompleteScreen.py")