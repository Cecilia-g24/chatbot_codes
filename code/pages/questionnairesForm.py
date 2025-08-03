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



q = config.QUESTIONNAIRES[st.session_state.next_q]




with st.form(f"q{q['id']}_form"):
    st.markdown(f"### 📝 Questionnaires ({q['id']}/9)")
    st.write(q["instructions"])

    answers = {}
    questions = getattr(config, q["qs"])
    labels = getattr(config, q["labels"])

    for key, question in questions.items():
        st.markdown(f"**({key})** {question}")
        answers[key] = st.radio(
            label="--------_",
            options=labels,
            index=None,
            key=f"matrix{q['id']}_radio_{key}",
            label_visibility="collapsed"
        )

    st.info(config.submit_warning)
    submitted = st.form_submit_button("Submit")

if submitted:
    response_key = f"q{q['id']}_responses"
    st.session_state[response_key] = answers

    path = os.path.join(config.TRANSCRIPTS_DIRECTORY, f"{st.session_state.username}.txt")
    with open(path, "a") as f:
        f.write(f"\n\n--- {q['title']} Responses ---\n")
        for key, value in st.session_state[response_key].items():
            f.write(f"{key}: {value}\n")

    st.success(f"✅ {q['title']} responses saved.")
    st.session_state.qnsubmitted = q["id"]
    st.switch_page("pages/qOrganizer.py")
