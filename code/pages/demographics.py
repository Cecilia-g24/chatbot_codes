import streamlit as st
import os
from utils import (
    check_password,
    check_if_interview_completed,
    save_questionnaire,
    check_prolific_access
)
import config
import random

st.set_page_config(page_title="demographics", page_icon="📝")


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

# Set a seed for consistent randomization across the session
if 'randomization_seed' not in st.session_state:
    st.session_state.randomization_seed = random.randint(1, 10000)

# Use the seed for consistent randomization
random.seed(st.session_state.randomization_seed)

# Generate two random booleans for consistent ordering decisions
trump_first = random.random() < 0.5
dem_first = random.random() < 0.5

# Set Trump/Harris order based on first random boolean
trump_harris_order = ["Donald Trump", "Kamala Harris"] if trump_first else ["Kamala Harris", "Donald Trump"]

# Create presidential vote options with randomized Trump/Harris order
presidential_options = trump_harris_order + ["Someone else", "I did not vote", "Prefer not to say"]
presidential_repeat_options = trump_harris_order + ["Someone else", "I would not vote", "Prefer not to say"]

# Set Democrat/Republican order based on second random boolean
dem_rep_order = ["Democrat", "Republican"] if dem_first else ["Republican", "Democrat"]

# Create political identification options with randomized Dem/Rep order
political_id_options = dem_rep_order + ["Independent", "Other", "No preference", "Prefer not to say"]

# Reset random seed to avoid affecting other parts of the code
random.seed()

st.title("📝 Questionnaire 1: Demographics")
st.success("Thank you for your effort! You finished the interview.")
st.success("To finish the study, please fill out this and the following questionnaires.")

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
    
    # Gender questions
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
        "ZIP/postal code (optional - only used to ensure that we represent all geographic regions of the country)",
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
    
    answers["employment_status"] = st.selectbox(
        "What is your current employment status?",
        options=[
            "Employed, full-time (35+ hours/week)",
            "Employed, part-time (1–34 hours/week)",
            "Self-employed (own business, farm, or freelance)",
            "Unemployed, actively looking for work",
            "Unemployed – on temporary layoff/furloughed",
            "Not in labor force – retired",
            "Not in labor force – student",
            "Not in labor force – homemaker/caregiver",
            "Not in labor force – unable to work due to disability/health",
            "Not in labor force – other reason (not seeking work)",
            "Other",
            "Prefer not to answer"
        ],
        index=None
    )

    answers["student_enrollment"] = st.selectbox(
        "Are you currently enrolled in school, college, or university?",
        options=[
            "No",
            "Yes, full-time",
            "Yes, part-time",
            "Prefer not to answer"
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
        "Who did you vote for in the LAST U.S. presidential election?",
        options=presidential_options,
        index=None
    )
    
    answers["presidential_vote_rep"] = st.radio(
        "If the U.S. presidential election was REPEATED TODAY, who would you vote for then?",
        options=presidential_repeat_options,
        index=None
    )
    
    # Political identification (with additional option)
    answers["political_id"] = st.radio(
        "How do you identify politically?",
        options=political_id_options,
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
        try:
            success = save_questionnaire(
                username=st.session_state.username,
                questionnaire_data=st.session_state.qdata,
                transcripts_directory=config.TRANSCRIPTS_DIRECTORY,
                file_name_addition="_demographics",
                max_attempts=100
            )
            
            if success:
                st.session_state.demographics_done = True
            else:
                st.error("❌ Unable to save questionnaire data after multiple attempts.")
                st.error("Please try submitting again or contact support if the problem persists.")
        except Exception as e:
                st.error(f"❌ Error saving questionnaire: {str(e)}")
                st.error("Please try submitting again or contact support.")

    else:
        st.info("Please fill out all required fields to continue.")


if st.session_state.demographics_done:
    st.session_state.test = st.session_state.username    
    st.switch_page("pages/qOrganizer.py")
