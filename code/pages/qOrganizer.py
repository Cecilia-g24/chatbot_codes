import streamlit as st
import os
import random
from utils import (
    check_password,
    check_if_interview_completed,
    save_interview_data,
    check_prolific_access
)
import config

st.set_page_config(page_title="qOrganizer", page_icon="🧠")

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

# Initialize the questionnaire list - randomize only on first run
if "selected_q_keys" not in st.session_state:
    # First time running - create randomized order
    #questionnaire_list = ["BFI10", "CAAS", "PIFS", "JIS", "ESS", "ATAS", "IUS12", "IE4", "TAM_AI"]
    questionnaire_list = ["IE4", "TAM_AI"]
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