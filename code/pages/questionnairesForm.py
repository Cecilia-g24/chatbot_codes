import streamlit as st
import os
from utils import (
    check_password,
    check_if_interview_completed,
    save_questionnaire,
    check_prolific_access
)
import config
import time

st.set_page_config(page_title="questionnaires", page_icon="🧠")
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



q = next(q for q in config.QUESTIONNAIRES if q["key"] == st.session_state.selected_q_keys[st.session_state.qcount])

# Initialize start time when questionnaire loads
if f"q{q['key']}_start_time" not in st.session_state:
    st.session_state[f"q{q['key']}_start_time"] = time.time()

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
            # Calculate timing data
            end_time = time.time()
            start_time = st.session_state[f"q{q['key']}_start_time"]
            time_spent = end_time - start_time

            success = save_questionnaire(
                username=st.session_state.username,
                questionnaire_data=st.session_state[response_key],
                transcripts_directory=config.TRANSCRIPTS_DIRECTORY,
                file_name_addition=f"_{q['key']}",
                max_attempts=100,
                start_time=start_time,
                end_time=end_time,
                time_spent=time_spent
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