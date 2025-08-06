import streamlit as st
import os
from utils import (
    check_password,
    check_if_interview_completed,
    save_questionnaire,
)
import config
st.set_page_config(page_title="questionnaires", page_icon="🧠")
# Auth + username
if config.LOGINS and True:  # test_Mode assumed True
    pwd_correct, username = check_password()
    if not pwd_correct:
        st.stop()
    st.session_state.username = username


q = next(q for q in config.QUESTIONNAIRES if q["key"] == st.session_state.selected_q_keys[st.session_state.qcount])

with st.form(f"q{q['key']}_form"):
    st.markdown(f"### 📝 Questionnaires ({st.session_state.qcount+1}/{st.session_state.numquests})")
    st.write(q["instructions"])
    
    answers = {}
    questions = q["questions"]  
    labels = q["labels"]        
    
    for key, question in questions.items():
        st.markdown(f"**({key})** {question}")
        answers[f"{q['key']}_{key}"] = st.radio(
            label="--------_",
            options=labels,
            index=None,
            key=f"matrix{q['key']}_radio_{key}",
            label_visibility="collapsed"
        )
    
    submitted = st.form_submit_button("Submit")

if submitted:
    allFilledOut = True
    for key, value in answers.items():
        if answers[key] == None:
            allFilledOut = False
    
    if allFilledOut:
        response_key = f"q{q['key']}_responses"
        st.session_state[response_key] = answers
                # Save to file
        try:
            success = save_questionnaire(
                username=st.session_state.username,
                questionnaire_data=st.session_state[response_key],
                transcripts_directory=config.TRANSCRIPTS_DIRECTORY,
                file_name_addition=f"_{q['key']}",
                max_attempts=100
            )
            
            if success:
                st.success(f"✅ {q['key']} responses saved.")  # Changed from q['title'] to q['key']
                st.switch_page("pages/qOrganizer.py")
            else:
                st.error("❌ Unable to save questionnaire data after multiple attempts.")
                st.error("Please try submitting again or contact support if the problem persists.")
        except Exception as e:
                st.error(f"❌ Error saving questionnaire: {str(e)}")
                st.error("Please try submitting again or contact support.")

        
        st.success(f"✅ {q['key']} responses saved.")  # Changed from q['title'] to q['key']
        st.switch_page("pages/qOrganizer.py")
    else:
        st.info("Please answer ALL questions to continue.")