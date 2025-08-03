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

with st.form("q1_form"):
    q1 = st.selectbox("1. What is your age?", options=list(range(18, 101)))
    q2 = st.radio("2. What is your gender?", ["Please select...", "Male", "Female", "Prefer to self-describe", "Prefer not to say"], index=None)
    q3 = st.selectbox("3. State of Residence", options=config.us_states, index=None)
    q5 = st.selectbox("5. Ethnicity / Race", ["White", "Black or African American", "Hispanic or Latino", "Asian", "Native American or Alaska Native", "Native Hawaiian or Pacific Islander", "Multiracial", "Other", "Prefer not to say"], index=None)
    q6 = st.selectbox("6. Highest level of education completed", ["Less than high school", "High school diploma or equivalent", "Some college, no degree", "Associate’s degree", "Bachelor’s degree", "Master’s degree", "Doctorate or professional degree", "Prefer not to say"], index=None)
    q7 = st.radio("7. How would you describe the area you live in?", ["Urban", "Urban/Rural Mix", "Rural"], index=None)
    q8 = st.selectbox("8. Current employment status", ["Employed full-time (more than 30 hrs/week)", "Employed part-time (8–29 hrs/week)", "Self-employed", "Unemployed, seeking work", "Not in labor force", "Retired", "Student", "Other"], index=None)
    q9 = st.selectbox("9. What is your current occupation?", options=config.occupations, index=None)
    q10 = st.selectbox("10. Industry or sector of your work", options=config.industry, index=None)
    q11 = st.radio("11. Total number of children", ["0", "1", "2", "3", "More than 3"], index=None)
    q12 = st.selectbox("12. What is your household size?", options=list(range(1, 10)), index=None)
    q13 = st.selectbox("13. Total annual household income (before tax)", ["Less than $10,000", "$10,000–19,999", "$20,000–29,999", "$30,000–39,999", "$40,000–49,999", "$50,000–59,999", "$60,000–74,999", "$75,000–99,999", "$100,000–124,999", "$125,000–149,999", "$150,000–199,999", "$200,000–249,999", "$250,000 or more", "Prefer not to answer"], index=None)
    q14 = st.radio("14. Who did you vote for in the last U.S. presidential election?", ["Donald Trump", "Kamala Harris", "Someone else", "I did not vote", "Prefer not to say"], index=None)
    q15 = st.radio("15. Political identification", ["Democrat", "Republican", "Independent", "Other", "Prefer not to say"], index=None)
    q19 = st.selectbox("19. Religious affiliation", ["None", "Christian – Protestant", "Christian – Catholic", "Other Christian", "Jewish", "Muslim", "Hindu", "Buddhist", "Other religion", "Prefer not to say"], index=None)
    q20 = st.radio("20. Are you a U.S. citizen?", ["Yes", "No", "Prefer not to say"], index=None)
    q21 = st.radio("21. Were you born in the United States?", ["Yes", "No", "Prefer not to say"], index=None)
    q22 = st.selectbox("22. Primary language at home", ["English", "Spanish", "Chinese", "Vietnamese", "Other", "Prefer not to say"], index=None)
    q23 = st.selectbox("23. Frequency of AI use", ["Multiple times a day", "Once a day", "A few times per week", "A few times per month", "Rarely", "Never", "I’m not sure"], index=None)

    st.info(config.submit_warning)
    submitted = st.form_submit_button("Submit")

if submitted:
    st.session_state.q1_responses = {
        #"username": st.session_state.username,
        "Age": q1,
        "Gender": q2,
        "State of Residence": q3,
        "Ethnicity / Race": q5,
        "Education": q6,
        "Area Type": q7,
        "Employment Status": q8,
        "Occupation": q9,
        "Industry": q10,
        "Number of Children": q11,
        "Household Size": q12,
        "Household Income": q13,
        "Presidential Vote": q14,
        "Political Identification": q15,
        "Religious Affiliation": q19,
        "US Citizen": q20,
        "Born in US": q21,
        "Primary Language": q22,
        "AI Use Frequency": q23,
    }

    path = os.path.join(config.TRANSCRIPTS_DIRECTORY, f"{st.session_state.username}.txt")
    with open(path, "a") as f:
        f.write("\n\n--- Questionnaire 1 (Demographics) Responses ---\n")
        for key, value in st.session_state["q1_responses"].items():
            f.write(f"{key}: {value}\n")

    st.success("✅ Questionnaire 1 responses saved.")
    st.session_state.demographics_done = True
    st.session_state.qnsubmitted = 1

if st.session_state.demographics_done:
    st.session_state.test = st.session_state.username    
    st.switch_page("pages/qOrganizer.py")
