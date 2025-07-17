import streamlit as st
import time
from utils import (
    check_password,
    check_if_interview_completed,
    save_interview_data,
)
import os
import config

from timer_display import show_countdown_timer_js

# Load API library
if "gpt" in config.MODEL.lower():
    api = "openai"
    from openai import OpenAI

else:
    raise ValueError(
        "Model does not contain 'gpt' or 'claude'; unable to determine API."
    )

# Set page title and icon
st.set_page_config(page_title="NIM Interview", page_icon=config.AVATAR_INTERVIEWER)

show_countdown_timer_js(timer_seconds=config.TIME_SETTING)

# Check if usernames and logins are enabled
if config.LOGINS:
    # Check password (displays login screen)
    pwd_correct, username = check_password()
    if not pwd_correct:
        st.stop()
    else:
        st.session_state.username = username
else:
    st.session_state.username = "testaccount"


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

if "closing_code_found" not in st.session_state:
    st.session_state.closing_code_found = None

if "questionnaire_submitted" not in st.session_state:
    st.session_state.questionnaire_submitted = False
if "matrix_submitted" not in st.session_state:
    st.session_state.matrix_submitted = False

# Check if interview previously completed
interview_previously_completed = check_if_interview_completed(
    config.TIMES_DIRECTORY, st.session_state.username
)

# If app started but interview was previously completed
if interview_previously_completed and not st.session_state.messages:
    st.session_state.interview_active = False
    completed_message = "Interview already completed."
    st.markdown(completed_message)


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


# add the demographic questionnaire section with streamlit's form function
# if condition: no code + q1 not submitted + q2 not submitted 
if st.session_state.closing_code_found and not st.session_state.questionnaire_submitted:
    with st.form("questionnaire_form"):
        st.markdown("### 📝 Part 2: Demographic Questionnaire")

        q1 = st.radio("1. What is your gender?", ["Male", "Female", "Other"])
        q2 = st.selectbox("2. What is your age?", options=list(range(18, 101)))
        q3 = st.radio("3. What is your highest level of education?", ["Secondary School", "Bachelor's Degree", "Master's Degree", "Doctorate"])
        q4 = st.radio("4. What is your current employment status?", ["Employed", "Unemployed", "Student", "Other"])
        q5 = st.radio("5. What is your average net monthly income?", ["1-1000", "1001-2000", "2001-5000", "5001+"])

        submitted = st.form_submit_button("Submit")
        if submitted:
            st.session_state.questionnaire_submitted = True
            st.session_state.questionnaire_responses = {
                    "Gender":      q1,
                    "Age":         q2,
                    "Education":   q3,
                    "Employment":  q4,
                    "Income":      q5
            }
            path = os.path.join(config.TRANSCRIPTS_DIRECTORY, f"{username}.txt")
            with open(path, "a") as f:
                f.write("\n\n--- Questionnaire Responses ---\n")
                for key, value in st.session_state["questionnaire_responses"].items():
                    f.write(f"{key}: {value}\n")
            st.success(config.complete_message_questionnaire)



# add VALUE ORIENTATION MATRIX SECTION
# if condition: no code + questionnaire submitted + matrix not submitted 
if st.session_state.closing_code_found and st.session_state.questionnaire_submitted and not st.session_state.matrix_submitted:
    
    with st.form("matrix_questionnaire_form"):
        st.markdown("### 🧭 Part 3: Value Orientation Questionnaire")
        st.write("Now I will briefly describe some people. Please use the slider to rank how much they are or are not like you.")

        matrix_answers = {}
        for key, question in config.likert_questions.items():
            st.markdown(f"**({key})** {question}")

            matrix_answers[key] = st.select_slider(
                label="",
                options=config.likert_labels,
                value=None,
                key=f"matrix_slider_{key}",
                label_visibility="collapsed"
            )

        submitted = st.form_submit_button("Submit")
        if submitted:
            st.session_state.matrix_submitted = True
            st.session_state.matrix_responses = matrix_answers

            path = os.path.join(config.TRANSCRIPTS_DIRECTORY, f"{username}.txt")
            with open(path, "a") as f:
                f.write("\n\n--- Value Orientation Responses ---\n")
                for key, value in st.session_state["matrix_responses"].items():
                    f.write(f"{key}: {value}\n")

            st.success(config.complete_message_valuematrix)



