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

with st.form("survey_form"):
    # Individual question definitions with descriptive field names
    answers = {}
    
    # === BASIC DEMOGRAPHICS ===
    
    # Age question
    answers["age"] = st.selectbox(
        "What is your age?",
        options=list(range(18, 120)),
        index=None
    )
    
    # Gender question
    answers["gender"] = st.radio(
        "What is your gender?",
        options=["Male", "Female", "Other", "Prefer not to say"],
        index=None
    )
    
    # State of residence
    answers["state"] = st.selectbox(
        "State of Residence",
        options=config.us_states,
        index=None
    )

    # ZIP code (optional)
    answers["zip_code"] = st.text_input(
        "ZIP/postal code (optional - only used to ensure that we represent all geographic regions of the the country)",
        max_chars=5,
        help="This helps us create maps showing geographic representation and ensure our research includes diverse regions across the country. Your ZIP code will only be used for aggregate geographic analysis.",
        placeholder="e.g., 90210"
    )
    
    
    # Ethnicity/Race
    answers["ethnicity"] = st.selectbox(
        "Ethnicity / Race",
        options=[
            "White", "Black or African American", "Hispanic or Latino", "Asian",
            "Native American or Alaska Native", "Native Hawaiian or Pacific Islander",
            "Multiracial", "Other", "Prefer not to say"
        ],
        index=None
    )
    
    # === HOUSEHOLD COMPOSITION ===
    
    # Marital/Relationship status
    answers["marital_status"] = st.radio(
        "What is your current marital or relationship status?",
        options=["Single, never married", "Married", "Living with partner", "Divorced", "Separated", "Widowed"],
        index=None
    )
    
    # Household size (extended range)
    answers["household_size"] = st.selectbox(
        "How many people, including yourself, do permanently live in your household?",
        options=list(range(1, 10)) + ["10 or more"],
        index=None
    )
    
    # Number of children (more specific)
    answers["children"] = st.radio(
        "Number of children under 18 living in your household",
        options=["0", "1", "2", "3", "More than 3"],
        index=None
    )
    
    # === GEOGRAPHIC/COMMUNITY CONTEXT ===
    
    # Area description
    answers["area_type"] = st.radio(
        "How would you describe the area you live in?",
        options=["Urban area", "Mixed urban-rural", "Rural area"],
        index=None
    )
    
    # Housing status
    answers["housing_status"] = st.radio(
        "What best describes your housing situation?",
        options=["Own home with mortgage", "Own home outright", "Rent", "Live with family/friends", "Other arrangement"],
        index=None
    )
    
    # === EDUCATION & WORK ===
    
    # Education level
    answers["education"] = st.selectbox(
        "Highest level of education completed",
        options=[
            "Less than high school", "High school diploma or equivalent", "Some college, no degree",
            "Associate's degree", "Bachelor's degree", "Master's degree",
            "Doctorate or professional degree", "Prefer not to say"
        ],
        index=None
    )
    
    # Employment status (with additional options)
    answers["employment_status"] = st.selectbox(
        "What is your current employment status?",
        options=[
            "Employed full-time (35+ hours/week)",
            "Employed part-time (less than 35 hours/week)",
            "Self-employed/Freelancer",
            "Unemployed, actively seeking work",
            "Unemployed, not seeking work",
            "On temporary leave",
            "Furloughed",
            "Retired",
            "Full-time student",
            "Homemaker/Caregiver",
            "Unable to work due to disability",
            "Other"
        ],
        index=None
    )
    
    # Occupation
    answers["occupation"] = st.selectbox(
        "What best describes your occupation, field of work, or intended career path? (If currently working: select your current job area. If not currently working: select your most recent job, your field of study, or intended career area)",
        options=[
            "Management/Executive",
            "Professional (Doctor, Lawyer, Engineer, Teacher, etc.)",
            "Healthcare Support",
            "Office/Administrative Support",
            "Sales",
            "Food Service/Hospitality",
            "Personal Care/Service",
            "Construction/Maintenance",
            "Production/Manufacturing",
            "Transportation/Material Moving",
            "Military/Police/Security/Emergency Services",
            "Arts/Entertainment/Media",
            "Information Technology/Computer Science",
            "Business/Finance",
            "Agriculture/Forestry/Fishing",
            "Undecided/Exploring options",
            "Never worked/No career plans yet",
            "Other"
        ],
        index=None
    )
    
    # === ECONOMIC INFORMATION ===
    
    # Household income
    answers["income"] = st.selectbox(
        "Total annual household income (before tax)",
        options=[
            "Less than $10,000", "$10,000–19,999", "$20,000–29,999", "$30,000–39,999",
            "$40,000–49,999", "$50,000–59,999", "$60,000–74,999", "$75,000–99,999",
            "$100,000–124,999", "$125,000–149,999", "$150,000–199,999",
            "$200,000–249,999", "$250,000 or more", "Prefer not to answer"
        ],
        index=None
    )
    
    
    # === CULTURAL/BACKGROUND ===
    
    # U.S. citizenship
    answers["us_citizen"] = st.radio(
        "Are you a U.S. citizen?",
        options=["Yes", "No", "Prefer not to say"],
        index=None
    )
    
    # Born in U.S.
    answers["born_in_us"] = st.radio(
        "Were you born in the United States?",
        options=["Yes", "No", "Prefer not to say"],
        index=None
    )
    
    # Primary language (expanded options)
    answers["primary_language"] = st.selectbox(
        "Primary language at home",
        options=[
            "English", "Spanish", "Chinese", "Vietnamese", "Arabic", 
            "Tagalog", "Korean", "Other", "Prefer not to say"
        ],
        index=None
    )
    
    # Religious affiliation
    answers["religion"] = st.selectbox(
        "Religious affiliation",
        options=[
            "None", "Christian – Protestant", "Christian – Catholic", "Other Christian",
            "Jewish", "Muslim", "Hindu", "Buddhist", "Other religion", "Prefer not to say"
        ],
        index=None
    )
    
    # === POLITICAL QUESTIONS ===
    
    # Presidential vote
    answers["presidential_vote"] = st.radio(
        "Who did you vote for in the last U.S. presidential election?",
        options=["Donald Trump", "Kamala Harris", "Someone else", "I did not vote", "Prefer not to say"],
        index=None
    )
    
    # Political identification (with additional option)
    answers["political_id"] = st.radio(
        "How do you identify politically?",
        options=["Democrat", "Republican", "Independent", "Other", "No preference", "Prefer not to say"],
        index=None
    )
    
    submitted = st.form_submit_button("Submit")

if submitted:
    # Define optional fields
    optional_fields = {"zip_code"}  # Add other optional fields here if needed
    
    # Check only required fields
    allRequiredFilled = True
    missing_fields = []
    
    for key, value in answers.items():
        if key not in optional_fields and (value is None or value == ""):
            allRequiredFilled = False
            missing_fields.append(key)
    
    if allRequiredFilled:
        # Save all responses (including optional ones that might be None/empty)
        for key, value in answers.items():
            st.session_state.qdata[key] = value
        
        # Save to file
        path = os.path.join(config.TRANSCRIPTS_DIRECTORY, f"{st.session_state.username}.txt")
        with open(path, "a") as f:
            f.write("\n\n--- Questionnaire 1 (Demographics) Responses ---\n")
            for key, value in st.session_state.qdata.items():
                # Handle None values gracefully
                display_value = value if value is not None else "Not provided"
                f.write(f"{key}: {display_value}\n")
        
        st.success("✅ Questionnaire 1 responses saved.")
        st.session_state.demographics_done = True
        st.session_state.qnsubmitted = 1
    else:
        st.info("Please fill out all required fields to continue.")
        # Optionally, you could show which fields are missing:
        # st.info(f"Please fill out these required fields: {', '.join(missing_fields)}")

if st.session_state.demographics_done:
    st.session_state.test = st.session_state.username    
    st.switch_page("pages/qOrganizer.py")
