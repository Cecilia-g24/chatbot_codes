import streamlit as st
import hmac
import time
import os
from datetime import datetime

def check_prolific_access():
    username = st.session_state.get("username")
    # Must be a non-empty string
    if not isinstance(username, str) or not username.strip():
        st.error("❌ Unauthorized access.")
        st.stop()
    return username

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


def check_if_interview_completed(directory, username, file_name_addition_transcript):
    """Check if interview transcript/time file exists which signals that interview was completed."""

    # Test account has multiple interview attempts
    if username != "testaccount":

        # Check if file exists
        try:
            with open(os.path.join(directory, f"{username}{file_name_addition_transcript}.txt"), "r") as _:
                return True

        except FileNotFoundError:
            return False

    else:

        return False


def save_interview_data(
    username,
    transcripts_directory,
    times_directory,
    file_name_addition_transcript='',
    file_name_addition_time=''
):
    """Write interview data (transcript and time) to disk."""
    transcripts_directory_file_path = os.path.join(transcripts_directory, f"{username}{file_name_addition_transcript}.txt")
    times_directory_file_path = os.path.join(times_directory, f"{username}{file_name_addition_time}.txt")
    # Store chat transcript
    with open(transcripts_directory_file_path,"w",encoding="utf-8") as t:
        t.write("Start of Chat Interview\n")
        for message in st.session_state.messages:
            if message['role'] in ["assistant","user"]:
                t.write(f"{message['role']}: {message['content']}\n")

    # Store file with start time and duration of interview
    with open(times_directory_file_path,"w",encoding="utf-8") as d:
        duration = (time.time() - st.session_state.start_time) / 60
        d.write(
            f"Start time (UTC): {time.strftime('%d/%m/%Y %H:%M:%S', time.localtime(st.session_state.start_time))}\nInterview duration (minutes): {duration:.2f}"
        )




def save_questionnaire(
    username,
    questionnaire_data,
    transcripts_directory,
    questionnaire_name="demographics",
    file_name_addition='',
    max_attempts=3,
    start_time=None,
    end_time=None,
    time_spent=None
):
    """Write questionnaire data to CSV with basic retry logic."""
    csv_file_path = os.path.join(transcripts_directory, f"{username}{file_name_addition}.csv")
         
    for attempt in range(max_attempts):
        try:
            # Prepare headers and values with username as first column
            timing_headers = []
            if start_time is not None:
                timing_headers = [f"start_time{file_name_addition}", f"end_time{file_name_addition}", f"time_spent_seconds{file_name_addition}"]
            headers = ["username"] + timing_headers + list(questionnaire_data.keys())
                         
            values = []
                         
            # Add username as first value
            username_escaped = username if username else "unknown"
            if ',' in username_escaped or '"' in username_escaped or '\n' in username_escaped:
                username_escaped = '"' + username_escaped.replace('"', '""') + '"'
            values.append(username_escaped)
                         
            # Add timing data if provided
            if start_time is not None:
                start_time_str = datetime.fromtimestamp(start_time).strftime("%Y-%m-%d %H:%M:%S")
                end_time_str = datetime.fromtimestamp(end_time).strftime("%Y-%m-%d %H:%M:%S")
                
                values.append(start_time_str)
                values.append(end_time_str)
                values.append(str(round(time_spent, 2)))
                         
            # Process questionnaire data values with CSV escaping
            for value in questionnaire_data.values():
                if value is None:
                    escaped_value = "NA"
                else:
                    str_value = str(value)
                                         
                    # If value contains comma, quote, or newline, wrap in quotes and escape internal quotes
                    if ',' in str_value or '"' in str_value or '\n' in str_value:
                        # Replace any existing quotes with double quotes (CSV standard)
                        str_value = str_value.replace('"', '""')
                        # Wrap the whole value in quotes
                        escaped_value = '"' + str_value + '"'
                    else:
                        escaped_value = str_value
                                 
                values.append(escaped_value)
                         
            # Check if file exists to determine if we need to write headers
            file_exists = os.path.exists(csv_file_path)
                         
            # Write CSV data using the same file writing pattern as your other functions
            with open(csv_file_path, "a", encoding="utf-8") as f:
                # Write headers only if file doesn't exist (first questionnaire for this user)
                if not file_exists:
                    f.write(",".join(headers) + "\n")
                                 
                # Write data row
                f.write(",".join(values) + "\n")
                         
            # Simple verification - check file exists and has content
            if os.path.exists(csv_file_path) and os.path.getsize(csv_file_path) > 0:
                return True  # Success!
            else:
                raise Exception("File verification failed - file empty or missing")
                         
        except (OSError, IOError, PermissionError) as e:
            # File system errors - worth retrying
            if attempt < max_attempts - 1:  # Not the last attempt
                time.sleep(0.1)  # Simple delay, no randomness needed
                continue
            else:
                raise Exception(f"Failed to save after {max_attempts} attempts. Last error: {str(e)}")
                 
        except Exception as e:
            # Unexpected errors - don't retry these
            raise Exception(f"Unexpected error saving questionnaire: {str(e)}")
         
    return False