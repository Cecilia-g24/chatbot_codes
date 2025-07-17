import streamlit as st
import hmac
import time
import os


# Password screen for dashboard (note: only very basic authentication!)
# Based on https://docs.streamlit.io/knowledge-base/deploy/authentication-without-sso
def check_password():
    """Returns 'True' if the user has entered a correct password."""

    def login_form():
        """Form with widgets to collect user information"""
        with st.form("Credentials"):
            st.text_input("Username", key="username")
            st.text_input("Password", type="password", key="password")
            st.form_submit_button("Log in", on_click=password_entered)

    def password_entered():
        """Checks whether username and password entered by the user are correct."""
        if st.session_state.username in st.secrets.passwords and hmac.compare_digest(
            st.session_state.password,
            st.secrets.passwords[st.session_state.username],
        ):
            st.session_state.password_correct = True

        else:
            st.session_state.password_correct = False

        del st.session_state.password  # don't store password in session state

    # Return True, username if password was already entered correctly before
    if st.session_state.get("password_correct", False):
        return True, st.session_state.username

    # Otherwise show login screen
    login_form()
    if "password_correct" in st.session_state:
        st.error("User or password incorrect")
    return False, st.session_state.username


def check_if_interview_completed(directory, username):
    """Check if interview transcript/time file exists which signals that interview was completed."""

    # Test account has multiple interview attempts
    if username != "testaccount":

        # Check if file exists
        try:
            with open(os.path.join(directory, f"{username}.txt"), "r") as _:
                return True

        except FileNotFoundError:
            return False

    else:

        return False


def save_interview_data(
    username,
    transcripts_directory,
    times_directory,
    file_name_addition_transcript="",
    file_name_addition_time="",
):
    """Write interview data (transcript and time) to disk."""

    # Store chat transcript
    with open(
        os.path.join(
            transcripts_directory, f"{username}{file_name_addition_transcript}.txt"
        ),
        "w",
    ) as t:
        for message in st.session_state.messages:
            t.write(f"{message['role']}: {message['content']}\n")

    # Store file with start time and duration of interview
    with open(
        os.path.join(times_directory, f"{username}{file_name_addition_time}.txt"),
        "w",
    ) as d:
        duration = (time.time() - st.session_state.start_time) / 60
        d.write(
            f"Start time (UTC): {time.strftime('%d/%m/%Y %H:%M:%S', time.localtime(st.session_state.start_time))}\nInterview duration (minutes): {duration:.2f}"
        )


########################### Test only, not used in main  ####################################
# adding the demographic & personality questionaire after the interview 
def display_questionnaire(username, save_directory):
    with st.form("questionnaire_form"):  # Fixed the form name (had a dot instead of underscore)
        st.markdown("## Demographic Questionnaire")  # Removed extra #
        q1 = st.radio("1. What is your gender?", ["Male", "Female", "Other"])
        q2 = st.text_input("2. What is your age?")  # Added missing closing parenthesis
        q3 = st.radio("3. Highest education?", ["Secondary", "Bachelor", "Master", "Doctorate"])
        q4 = st.radio("4. Employment status?", ["Employee", "Student", "Other"])
        q5 = st.radio("5. Monthly income?", ["1-1000", "1001-2000", "2001+"])
        submitted = st.form_submit_button("Submit")
        print("submitt: "+str(submitted))
        if submitted:
            try:
                path = os.path.join(save_directory, f"{username}_dsfdsf.txt")  # Changed from "./data" to save_directory
                with open(path, "a") as f:
                    f.write("\n\n--- Questionnaire Responses ---\n")
                    f.write(f"1. Gender: {q1}\n2. Age: {q2}\n3. Education: {q3}\n4. Employment: {q4}\n5. Income: {q5}\n")
                st.success("Thank you for your feedback!")
                st.session_state.questionnaire_submitted = True  # Fixed variable name (removed underscore prefix)
            except Exception as e:
                st.error("Failed to save.")
                print(f"Error: {e}")  # Added proper error logging



