import streamlit as st
import time
from utils import (
    check_password,
    check_if_interview_completed,
    save_interview_data,
)
import os
import config
from timer_display import show_countdown_timer_js         # for countdown timer 


# Set page title and icon
st.set_page_config(page_title="NIM Interview", page_icon=config.AVATAR_INTERVIEWER)


# Extract Prolific parameters from URL 
query_params = st.query_params
prolific_pid = query_params.get("PROLIFIC_PID", [None])
study_id = query_params.get("STUDY_ID", [None])
session_id = query_params.get("SESSION_ID", [None])


# on-screen display to show prolific id
if prolific_pid:
    st.markdown(f"👤 Prolific PID: `{prolific_pid}`")


# Load API library
if "gpt" in config.MODEL.lower():
    api = "openai"
    from openai import OpenAI
else:
    raise ValueError(
        "Model does not contain 'gpt' or 'claude'; unable to determine API."
    )


# show timer on screen, function imported from timer_display.py
show_countdown_timer_js(timer_seconds=config.TIME_SETTING)


# Check if usernames and logins are enabled
if config.LOGINS:
    pwd_correct, username = check_password()
    if not pwd_correct:
        st.stop()
    else:
        st.session_state.username = username
# set prolific_pid = username, when login function is disabled
else:
    st.session_state.username = prolific_pid or "testaccount"



# Create directories if they do not already exist
if not os.path.exists(config.TRANSCRIPTS_DIRECTORY):
    os.makedirs(config.TRANSCRIPTS_DIRECTORY)
if not os.path.exists(config.TIMES_DIRECTORY):
    os.makedirs(config.TIMES_DIRECTORY)
if not os.path.exists(config.BACKUPS_DIRECTORY):
    os.makedirs(config.BACKUPS_DIRECTORY)

# Initialise session state
if "interview_active" not in st.session_state:
    st.session_state.interview_active = True

# Initialise messages list in session state
if "messages" not in st.session_state:
    st.session_state.messages = []

# Store start time in session state
if "start_time" not in st.session_state:
    st.session_state.start_time = time.time()
    st.session_state.start_time_file_names = time.strftime(
        "%Y_%m_%d_%H_%M_%S", time.localtime(st.session_state.start_time)
    )


# Initialize closing code for ending interview
if "closing_code_found" not in st.session_state:
    st.session_state.closing_code_found = None
# Initialize questionnaire step flags for state control 
if "qnsubmitted" not in st.session_state:
    st.session_state.qnsubmitted = 0


# Check if interview previously completed
interview_previously_completed = check_if_interview_completed(
    config.TIMES_DIRECTORY, st.session_state.username
)


# If app started but interview was previously completed
if interview_previously_completed and not st.session_state.messages:
    st.session_state.interview_active = False
    completed_message = "Interview already completed."
    st.warning(completed_message)


# Add 'Quit' button to dashboard
col1, col2 = st.columns([0.85, 0.15])
# Place where the second column is
with col2:
    # If interview is active and 'Quit' button is clicked
    if st.session_state.interview_active and st.button(
        "Quit", help="End the interview."
    ):
        # Set interview to inactive, display quit message, and store data
        st.session_state.interview_active = False
        quit_message = "You have cancelled the interview."
        st.session_state.messages.append({"role": "assistant", "content": quit_message})
        save_interview_data(
            st.session_state.username,
            config.TRANSCRIPTS_DIRECTORY,
            config.TIMES_DIRECTORY,
        )


# Upon rerun, display the previous conversation (except system prompt or first message)
for message in st.session_state.messages[1:]:
    if message["role"] == "assistant":
        avatar = config.AVATAR_INTERVIEWER
    else:
        avatar = config.AVATAR_RESPONDENT
    # Only display messages without codes
    if not any(code in message["content"] for code in config.CLOSING_MESSAGES.keys()):
        with st.chat_message(message["role"], avatar=avatar):
            st.markdown(message["content"])

# Load API client
if api == "openai":
    client = OpenAI(api_key=os.environ.get('OPENAI_API_KEY', st.secrets["API_KEY_OPENAI"]))
    api_kwargs = {"stream": True}

# API kwargs
api_kwargs["messages"] = st.session_state.messages
api_kwargs["model"] = config.MODEL
api_kwargs["max_tokens"] = config.MAX_OUTPUT_TOKENS
if config.TEMPERATURE is not None:
    api_kwargs["temperature"] = config.TEMPERATURE

# In case the interview history is still empty, pass system prompt to model, and generate and display its first message
if not st.session_state.messages:
    if api == "openai":
        st.session_state.messages.append({"role": "system", "content": config.SYSTEM_PROMPT})
        with st.chat_message("assistant", avatar=config.AVATAR_INTERVIEWER):
            stream = client.chat.completions.create(**api_kwargs)
            message_interviewer = st.write_stream(stream)

    st.session_state.messages.append({"role": "assistant", "content": message_interviewer})

    # Store first backup files to record who started the interview
    save_interview_data(
        username=st.session_state.username,
        transcripts_directory=config.BACKUPS_DIRECTORY,
        times_directory=config.BACKUPS_DIRECTORY,
        file_name_addition_transcript=f"_transcript_started_{st.session_state.start_time_file_names}",
        file_name_addition_time=f"_time_started_{st.session_state.start_time_file_names}",
    )


# --- Add time-out and warning logic ---
elapsed_time = int(time.time() - st.session_state.start_time)
remaining_time = config.TIME_SETTING - elapsed_time

# Show warning if less than 60 seconds left and interview still active
if 0 < remaining_time <= 60 and st.session_state.interview_active:
    st.warning(
        f"⚠️ Only {remaining_time} seconds left for Part 1. Please wrap up your response.",
        icon="⚠️"
    )

# If time is up, end the interview
if remaining_time <= 0 and st.session_state.interview_active:
    st.session_state.interview_active = False
    st.markdown("⏰ **Time is up. The interview has been terminated automatically.**")
    save_interview_data(
        username=st.session_state.username,
        transcripts_directory=config.TRANSCRIPTS_DIRECTORY,
        times_directory=config.TIMES_DIRECTORY,
    )



# Main chat if interview is active
if st.session_state.interview_active:
    # Chat input and message for respondent
    if message_respondent := st.chat_input("Your message here"):
        st.session_state.messages.append({"role": "user", "content": message_respondent})

        # Display respondent message
        with st.chat_message("user", avatar=config.AVATAR_RESPONDENT):
            st.markdown(message_respondent)

        # Generate and display interviewer message
        with st.chat_message("assistant", avatar=config.AVATAR_INTERVIEWER):
            # Create placeholder for message in chat interface
            message_placeholder = st.empty()

            # Initialise message of interviewer
            message_interviewer = ""

            if api == "openai":
                # Stream responses
                stream = client.chat.completions.create(**api_kwargs)
                for message in stream:
                    text_delta = message.choices[0].delta.content
                    if text_delta is not None:
                        message_interviewer += text_delta
                    # Start displaying message only after 5 characters to first check for codes
                    if len(message_interviewer) > 5:
                        message_placeholder.markdown(message_interviewer + "▌")
                    if any(code in message_interviewer for code in config.CLOSING_MESSAGES.keys()):
                        message_placeholder.empty()
                        break


            # Determine whether the message contains a closing code
            closing_code_found = next(
                (code for code in config.CLOSING_MESSAGES.keys() if code in message_interviewer), None
            )

            if closing_code_found:
                message_placeholder.empty()
                st.session_state.messages.append({"role": "assistant", "content": message_interviewer})
                st.session_state.closing_code_found = closing_code_found
            
            # Then continue final closing
                st.session_state.interview_active = False
                closing_message = config.CLOSING_MESSAGES[closing_code_found]
                st.markdown(closing_message)
                st.session_state.messages.append(
                        {"role": "assistant", "content": closing_message}
                    )

                # Store final transcript and time
                final_transcript_stored = False
                while not final_transcript_stored:
                        save_interview_data(
                            username=st.session_state.username,
                            transcripts_directory=config.TRANSCRIPTS_DIRECTORY,
                            times_directory=config.TIMES_DIRECTORY,
                        )
                        final_transcript_stored = check_if_interview_completed(
                            config.TRANSCRIPTS_DIRECTORY, st.session_state.username
                        )
                        time.sleep(0.1)
                st.rerun()

            else:
                # If no code is in the message, display and store the message
                message_placeholder.markdown(message_interviewer)
                st.session_state.messages.append(
                    {"role": "assistant", "content": message_interviewer}
                )

                # Regularly store interview progress as backup, but prevent script from
                # stopping in case of a write error
                try:
                    save_interview_data(
                        username=st.session_state.username,
                        transcripts_directory=config.BACKUPS_DIRECTORY,
                        times_directory=config.BACKUPS_DIRECTORY,
                        file_name_addition_transcript=f"_transcript_started_{st.session_state.start_time_file_names}",
                        file_name_addition_time=f"_time_started_{st.session_state.start_time_file_names}",
                    )
                except:
                    pass


# Q1: demographics questionnaire (Post-Interview Questionnaire on AI and Economic Outlook) 
# if condition: yes closing code + no qs submitted
if st.session_state.closing_code_found and st.session_state.qnsubmitted == 0:
    with st.form("q1_form"):
        st.markdown("### 📝 Questionnaires (1/9)")


        # 1. Age
        q1 = st.selectbox("1. What is your age?", options=list(range(18, 101)))

        # 2. Gender
        q2 = st.radio("2. What is your gender?", 
                      ["Male", "Female", "Prefer to self-describe", "Prefer not to say"])

        # 3. State of Residence
        q3 = st.selectbox("3. State of Residence", options=config.us_states)

        # 4. Zip Code 
        #q4 = st.text_input("4. Zip Code (5-digit)", value="", key= "type your response here")

        # 5. Ethnicity / Race
        q5 = st.selectbox(
            "5. Ethnicity / Race",
            ["White","Black or African American","Hispanic or Latino","Asian",
             "Native American or Alaska Native","Native Hawaiian or Pacific Islander",
             "Multiracial","Other","Prefer not to say"]
        )

        # 6. Education
        q6 = st.selectbox(
            "6. Highest level of education completed",
            ["Less than high school","High school diploma or equivalent",
             "Some college, no degree","Associate’s degree","Bachelor’s degree",
             "Master’s degree","Doctorate or professional degree","Prefer not to say"]
        )

        # 7. Area type
        q7 = st.radio("7. How would you describe the area you live in?",
                      ["Urban","Urban/Rural Mix","Rural"])

        # 8. Employment status
        q8 = st.selectbox(
            "8. Current employment status",
            ["Employed full-time (more than 30 hrs/week)","Employed part-time (8–29 hrs/week)","Self-employed",
             "Unemployed, seeking work","Not in labor force","Retired","Student","Other"]
        )

        # 9. Occupation
        q9 = st.selectbox("9. What is your current occupation?", options=config.occupations)

        # 10. Industry
        q10 = st.selectbox("10. Industry or sector of your work", options=config.industry)

        # 11. Number of children
        q11 = st.radio("11. Total number of children", ["0","1","2","3","More than 3"])

        # 12. Household size
        q12 = st.selectbox("12. What is your household size?", options=list(range(1, 10)))

        # 13. Household income
        q13 = st.selectbox(
            "13. Total annual household income (before tax)",
            ["Less than $10,000","$10,000–19,999","$20,000–29,999","$30,000–39,999","$40,000–49,999",
             "$50,000–59,999","$60,000–74,999","$75,000–99,999","$100,000–124,999",
             "$125,000–149,999","$150,000–199,999","$200,000–249,999","$250,000 or more",
             "Prefer not to answer"]
        )

        # 14. Presidential vote
        q14 = st.radio("14. Who did you vote for in the last U.S. presidential election?",
                       ["Donald Trump","Kamala Harris","Someone else","I did not vote","Prefer not to say"])

        # 15. Political identification
        q15 = st.radio("15. Political identification",
                       ["Democrat","Republican","Independent","Other","Prefer not to say"])

        # 19. Religious affiliation
        q19 = st.selectbox("19. Religious affiliation",
                           ["None","Christian – Protestant","Christian – Catholic","Other Christian",
                            "Jewish","Muslim","Hindu","Buddhist","Other religion","Prefer not to say"])

        # 20. U.S. citizenship
        q20 = st.radio("20. Are you a U.S. citizen?",
                       ["Yes","No","Prefer not to say"])

        # 21. Born in U.S.
        q21 = st.radio("21. Were you born in the United States?",
                       ["Yes","No","Prefer not to say"])

        # 22. Primary language
        q22 = st.selectbox("22. Primary language at home",
                           ["English","Spanish","Chinese","Vietnamese","Other","Prefer not to say"])

        # 23. Frequency of AI use
        q23 = st.selectbox("23. Frequency of AI use",
                           ["Multiple times a day","Once a day","A few times per week","A few times per month",
                            "Rarely","Never","I’m not sure"])

        ##############################
        st.info(config.submit_warning)
        submitted = st.form_submit_button("Submit")

        if submitted:
            st.session_state.q1_responses = {
                "Age": q1,
                "Gender": q2,
                "State of Residence": q3,
                #"Zip Code": q4,
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
                "AI Use Frequency": q23
            }

            path = os.path.join(config.TRANSCRIPTS_DIRECTORY, f"{st.session_state.username}.txt")
            with open(path, "a") as f:
                f.write("\n\n--- Questionnaire 1 (Demographics) Responses ---\n")
                for key, value in st.session_state["q1_responses"].items():
                    f.write(f"{key}: {value}\n")
            st.success("Questionnaire 1 responses Saved")
            st.session_state.qnsubmitted  = 1


# Q2: personality questionnaire (ESS)
# if condition: yes closing code + q1 submitted 
if st.session_state.closing_code_found and st.session_state.qnsubmitted == 1:
    with st.form("q2_form"):
        st.markdown("### 📝 Questionnaires (2/9)")

        st.write("Now I will briefly describe some people. Please use the slider to rank how much they are or are not like you.")

        q2_answers = {}
        for key, question in config.q2_qs.items():
            st.markdown(f"**({key})** {question}")

            q2_answers[key] = st.select_slider(
                label="--------_",
                options=config.q2_labels,
                value=None,
                key=f"matrix2_slider_{key}",
                label_visibility="collapsed"
            )

        st.info(config.submit_warning)
        submitted = st.form_submit_button("Submit")
        if submitted:
            st.session_state.q2_responses = q2_answers

            path = os.path.join(config.TRANSCRIPTS_DIRECTORY, f"{st.session_state.username}.txt")
            with open(path, "a") as f:
                f.write("\n\n--- Questionnaire 2 (ESS) Responses  ---\n")
                for key, value in st.session_state["q2_responses"].items():
                    f.write(f"{key}: {value}\n")

            st.success("Questionnaire 2 responses Saved")
            st.session_state.qnsubmitted  = 2


# Q3: personality questionnaire (ATAS)
# if condition: yes closing code + q2 submitted 
if st.session_state.closing_code_found and st.session_state.qnsubmitted == 2:
    with st.form("q3_form"):
        st.markdown("### 📝 Questionnaires (3/9)")
        st.write("Please respond to each prompt with the appropriate level of agreement per your personal feelings about yourself and technology.")

        q3_answers = {}
        for key, question in config.q3_qs.items():
            st.markdown(f"**({key})** {question}")

            q3_answers[key] = st.select_slider(
                label="--------_",
                options=config.q3_labels,
                value=None,
                key=f"matrix3_slider_{key}",
                label_visibility="collapsed"
            )

        st.info(config.submit_warning)
        submitted = st.form_submit_button("Submit")
        if submitted:
            st.session_state.q3_responses = q3_answers

            path = os.path.join(config.TRANSCRIPTS_DIRECTORY, f"{st.session_state.username}.txt")
            with open(path, "a") as f:
                f.write("\n\n--- Questionnaire 3 (ATAS) Responses ---\n")
                for key, value in st.session_state["q3_responses"].items():
                    f.write(f"{key}: {value}\n")

            st.success("Questionnaire 3 responses Saved")
            st.session_state.qnsubmitted  = 3


# Q4: personality questionnaire (ASKU)
# if condition: yes closing code + q3 submitted 
if st.session_state.closing_code_found and st.session_state.qnsubmitted == 3:
    with st.form("q4_form"):
        st.markdown("### 📝 Questionnaires (4/9)")
        st.write("The following statements may apply more or less to you. To what extent do you think each statement applies to you personally?")
        q4_answers = {}
        for key, question in config.q4_qs.items():
            st.markdown(f"**({key})** {question}")

            q4_answers[key] = st.select_slider(
                label="--------_",
                options=config.q4_labels,
                value=None,
                key=f"matrix4_slider_{key}",
                label_visibility="collapsed"
            )

        st.info(config.submit_warning)
        submitted = st.form_submit_button("Submit")
        if submitted:
            st.session_state.q4_responses = q4_answers

            path = os.path.join(config.TRANSCRIPTS_DIRECTORY, f"{st.session_state.username}.txt")
            with open(path, "a") as f:
                f.write("\n\n--- Questionnaire 4 (ASKU) Responses ---\n")
                for key, value in st.session_state["q4_responses"].items():
                    f.write(f"{key}: {value}\n")

            st.success("Questionnaire 4 responses Saved")
            st.session_state.qnsubmitted  = 4


# Q5: personality questionnaire (IE-4)
# if condition: yes closing code + q4 submitted 
if st.session_state.closing_code_found and st.session_state.qnsubmitted == 4:
    with st.form("q5_form"):
        st.markdown("### 📝 Questionnaires (5/9)")
        st.write("The following statements may apply more or less to you. To what extent do you think each statement applies to you personally?")
        q5_answers = {}
        for key, question in config.q5_qs.items():
            st.markdown(f"**({key})** {question}")

            q5_answers[key] = st.select_slider(
                label="--------_",
                options=config.q5_labels,
                value=None,
                key=f"matrix5_slider_{key}",
                label_visibility="collapsed"
            )

        st.info(config.submit_warning)
        submitted = st.form_submit_button("Submit")
        if submitted:
            st.session_state.q5_responses = q5_answers

            path = os.path.join(config.TRANSCRIPTS_DIRECTORY, f"{st.session_state.username}.txt")
            with open(path, "a") as f:
                f.write("\n\n--- Questionnaire 5 (IE-4) Responses ---\n")
                for key, value in st.session_state["q5_responses"].items():
                    f.write(f"{key}: {value}\n")

            st.success("Questionnaire 5 responses Saved")
            st.session_state.qnsubmitted  = 5


# Q6: personality questionnaire (L-1)
# if condition: yes closing code + q5 submitted 
if st.session_state.closing_code_found and st.session_state.qnsubmitted == 5:
    with st.form("q6_form"):
        st.markdown("### 📝 Questionnaires (6/9)")
        st.write("The next question is about your general satisfaction with life.")
        q6_answers = {}
        for key, question in config.q6_qs.items():
            st.markdown(f"**({key})** {question}")

            q6_answers[key] = st.select_slider(
                label="--------_",
                options=config.q6_labels,
                value=None,
                key=f"matrix6_slider_{key}",
                label_visibility="collapsed"
            )

        st.info(config.submit_warning)
        submitted = st.form_submit_button("Submit")
        if submitted:
            st.session_state.q6_responses = q6_answers

            path = os.path.join(config.TRANSCRIPTS_DIRECTORY, f"{st.session_state.username}.txt")
            with open(path, "a") as f:
                f.write("\n\n--- Questionnaire 6 (L-1) Responses ---\n")
                for key, value in st.session_state["q6_responses"].items():
                    f.write(f"{key}: {value}\n")

            st.success("Questionnaire 6 responses Saved")
            st.session_state.qnsubmitted  = 6


# Q7: personality questionnaire (BFI-10)
# if condition: yes closing code + q6 submitted 
if st.session_state.closing_code_found and st.session_state.qnsubmitted == 6:
    with st.form("q7_form"):
        st.markdown("### 📝 Questionnaires (7/9)")
        st.write("How well do the following statements describe your personality? I see myself as someone who…")

        q7_answers = {}
        for key, question in config.q7_qs.items():
            st.markdown(f"**({key})** {question}")

            q7_answers[key] = st.select_slider(
                label="--------_",
                options=config.q7_labels,
                value=None,
                key=f"matrix7_slider_{key}",
                label_visibility="collapsed"
            )

        st.info(config.submit_warning)
        submitted = st.form_submit_button("Submit")
        if submitted:
            st.session_state.q7_responses = q7_answers

            path = os.path.join(config.TRANSCRIPTS_DIRECTORY, f"{st.session_state.username}.txt")
            with open(path, "a") as f:
                f.write("\n\n--- Questionnaire 7 (BFI-10) Responses  ---\n")
                for key, value in st.session_state["q7_responses"].items():
                    f.write(f"{key}: {value}\n")

            st.success("Questionnaire 7 responses Saved")
            st.session_state.qnsubmitted  = 7


# Q8: personality questionnaire (ICT-SC25e)
# if condition: yes closing code + q7 submitted 
if st.session_state.closing_code_found and st.session_state.qnsubmitted == 7:
    with st.form("q8_form"):
        st.markdown("### 📝 Questionnaires (8/9)")
        st.write("In the following, you will be asked questions about the handling of digital systems. Digital systems are all digital applications (e.g., software or apps) and all digital devices (e.g., computers or smartphones).")

        q8_answers = {}
        for key, question in config.q8_qs.items():
            st.markdown(f"**({key})** {question}")

            q8_answers[key] = st.select_slider(
                label="--------_",
                options=config.q8_labels,
                value=None,
                key=f"matrix8_slider_{key}",
                label_visibility="collapsed"
            )

        st.info(config.submit_warning)
        submitted = st.form_submit_button("Submit")
        if submitted:
            st.session_state.q8_responses = q8_answers

            path = os.path.join(config.TRANSCRIPTS_DIRECTORY, f"{st.session_state.username}.txt")
            with open(path, "a") as f:
                f.write("\n\n--- Questionnaire 8 (ICT-SC25e) Responses  ---\n")
                for key, value in st.session_state["q8_responses"].items():
                    f.write(f"{key}: {value}\n")

            st.success("Questionnaire 8 responses Saved")
            st.session_state.qnsubmitted  = 8


# Q9: personality questionnaire (Technophobie)
# if condition: yes closing code + q8 submitted 
if st.session_state.closing_code_found and st.session_state.qnsubmitted == 8:
    with st.form("q9_form"):
        st.markdown("### 📝 Questionnaires (9/9)")
        st.write("Please indicate by marking the appropriate number between 1 and 5 how much these statements apply to you. Assign the value 1 if the statement applies strongly to you (applies strongly) and the value 5 if the statement does not apply to you at all (does not apply at all).")

        q9_answers = {}
        for key, question in config.q9_qs.items():
            st.markdown(f"**({key})** {question}")

            q9_answers[key] = st.select_slider(
                label="--------_",
                options=config.q9_labels,
                value=None,
                key=f"matrix9_slider_{key}",
                label_visibility="collapsed"
            )

        st.info(config.submit_warning)
        submitted = st.form_submit_button("Submit")
        if submitted:
            st.session_state.q9_responses = q9_answers

            path = os.path.join(config.TRANSCRIPTS_DIRECTORY, f"{st.session_state.username}.txt")
            with open(path, "a") as f:
                f.write("\n\n--- Questionnaire 9 (Technophobie) Responses  ---\n")
                for key, value in st.session_state["q9_responses"].items():
                    f.write(f"{key}: {value}\n")

            st.success("Questionnaire 9 responses Saved")
            st.session_state.qnsubmitted  = 9



# provide prolific redirection link 
# if condition: yes closing code + q9 submitted  
if st.session_state.closing_code_found and st.session_state.qnsubmitted == 9:
    st.success("You have completed the study. Please return to Prolific and submit your completion code.")
    if st.button("Return to Prolific"):
        st.markdown(
            f'<meta http-equiv="refresh" content="0; url={config.prolific_completion_url}">',
            unsafe_allow_html=True,
        )