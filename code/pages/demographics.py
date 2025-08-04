import streamlit as st
import os
from utils import (
    check_password,
    check_if_interview_completed,
    save_interview_data,
)
import config

st.set_page_config(page_title="demographics", page_icon="📝")


# Auth + username
if config.LOGINS and True:  # test_Mode assumed True
    pwd_correct, username = check_password()
    if not pwd_correct:
        st.stop()
    st.session_state.username = username

st.title("📝 Questionnaire 1: Demographics")

# Initialise session state
if "demographics_done" not in st.session_state:
    st.session_state.demographics_done = False

if "qdata" not in st.session_state:
    st.session_state.qdata = {}

with st.form("q1_form"):
    # List of questions
    question_definitions = {
        "q1": {
            "label": "1. What is your age?",
            "type": "selectbox",
            "options": list(range(18, 120))
        },
        "q2": {
            "label": "2. What is your gender?",
            "type": "radio",
            "options": ["Please select...", "Male", "Female", "Prefer to self-describe", "Prefer not to say"]
        },
        "q3": {
            "label": "3. State of Residence",
            "type": "selectbox",
            "options": config.us_states
        },
        "q5": {
            "label": "5. Ethnicity / Race",
            "type": "selectbox",
            "options": [
                "White", "Black or African American", "Hispanic or Latino", "Asian",
                "Native American or Alaska Native", "Native Hawaiian or Pacific Islander",
                "Multiracial", "Other", "Prefer not to say"
            ]
        },
        "q6": {
            "label": "6. Highest level of education completed",
            "type": "selectbox",
            "options": [
                "Less than high school", "High school diploma or equivalent", "Some college, no degree",
                "Associate’s degree", "Bachelor’s degree", "Master’s degree",
                "Doctorate or professional degree", "Prefer not to say"
            ]
        },
        "q7": {
            "label": "7. How would you describe the area you live in?",
            "type": "radio",
            "options": ["Urban", "Urban/Rural Mix", "Rural"]
        },
        "q8": {
            "label": "8. Current employment status",
            "type": "selectbox",
            "options": [
                "Employed full-time (more than 30 hrs/week)", "Employed part-time (8–29 hrs/week)",
                "Self-employed", "Unemployed, seeking work", "Not in labor force",
                "Retired", "Student", "Other"
            ]
        },
        "q9": {
            "label": "9. What is your current occupation?",
            "type": "selectbox",
            "options": config.occupations
        },
        "q10": {
            "label": "10. Industry or sector of your work",
            "type": "selectbox",
            "options": config.industry
        },
        "q11": {
            "label": "11. Total number of children",
            "type": "radio",
            "options": ["0", "1", "2", "3", "More than 3"]
        },
        "q12": {
            "label": "12. What is your household size?",
            "type": "selectbox",
            "options": list(range(1, 10))
        },
        "q13": {
            "label": "13. Total annual household income (before tax)",
            "type": "selectbox",
            "options": [
                "Less than $10,000", "$10,000–19,999", "$20,000–29,999", "$30,000–39,999",
                "$40,000–49,999", "$50,000–59,999", "$60,000–74,999", "$75,000–99,999",
                "$100,000–124,999", "$125,000–149,999", "$150,000–199,999",
                "$200,000–249,999", "$250,000 or more", "Prefer not to answer"
            ]
        },
        "q14": {
            "label": "14. Who did you vote for in the last U.S. presidential election?",
            "type": "radio",
            "options": ["Donald Trump", "Kamala Harris", "Someone else", "I did not vote", "Prefer not to say"]
        },
        "q15": {
            "label": "15. Political identification",
            "type": "radio",
            "options": ["Democrat", "Republican", "Independent", "Other", "Prefer not to say"]
        },
        "q19": {
            "label": "19. Religious affiliation",
            "type": "selectbox",
            "options": [
                "None", "Christian – Protestant", "Christian – Catholic", "Other Christian",
                "Jewish", "Muslim", "Hindu", "Buddhist", "Other religion", "Prefer not to say"
            ]
        },
        "q20": {
            "label": "20. Are you a U.S. citizen?",
            "type": "radio",
            "options": ["Yes", "No", "Prefer not to say"]
        },
        "q21": {
            "label": "21. Were you born in the United States?",
            "type": "radio",
            "options": ["Yes", "No", "Prefer not to say"]
        },
        "q22": {
            "label": "22. Primary language at home",
            "type": "selectbox",
            "options": ["English", "Spanish", "Chinese", "Vietnamese", "Other", "Prefer not to say"]
        },
        "q23": {
            "label": "23. Frequency of AI use",
            "type": "selectbox",
            "options": [
                "Multiple times a day", "Once a day", "A few times per week",
                "A few times per month", "Rarely", "Never", "I’m not sure"
            ]
        }
    }


    # Loop through the questions
    answers = {}
    for key, q in question_definitions.items():
        if q["type"] == "selectbox":
            answers[key] = st.selectbox(q["label"], options=q["options"], index=None)
        elif q["type"] == "radio":
            answers[key] = st.radio(q["label"], options=q["options"], index=None)

    st.info(config.submit_warning)
    submitted = st.form_submit_button("Submit")

if submitted:
    allFilledOut = True
    for key, value in answers.items():
        if answers[key]==None: 
            allFilledOut = False
    
    if allFilledOut:
        for key, value in answers.items():
            st.session_state.qdata[key] = value

        path = os.path.join(config.TRANSCRIPTS_DIRECTORY, f"{st.session_state.username}.txt")
        with open(path, "a") as f:
            f.write("\n\n--- Questionnaire 1 (Demographics) Responses ---\n")
            for key, value in st.session_state.qdata.items():
                f.write(f"{key}: {value}\n")

        st.success("✅ Questionnaire 1 responses saved.")
        st.session_state.demographics_done = True
        st.session_state.qnsubmitted = 1
    else:
        st.info("Please fill out all fields to continue.")

if st.session_state.demographics_done:
    st.session_state.test = st.session_state.username    
    st.switch_page("pages/qOrganizer.py")
