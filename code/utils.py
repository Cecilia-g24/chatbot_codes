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


def display_countdown_timer(start_time, interview_duration=120, warning_threshold=60):



    """
    Displays a countdown timer in the top-right corner of the Streamlit app.
    
    Args:
        start_time (float): Time when interview started (from time.time())
        interview_duration (int): Total interview duration in seconds (default: 120)
        warning_threshold (int): When to show warning (default: 60 seconds)
        
    Returns:
        float: Time remaining in seconds
    """
    time_elapsed = time.time() - start_time
    time_remaining = max(interview_duration - time_elapsed, 0)
    
    # Format time display
    mins, secs = divmod(int(time_remaining), 60)
    timer_display = f"{mins:02d}:{secs:02d}"
    
    # Create warning message if time is running low
    warning_html = ""
    if time_remaining <= warning_threshold and time_remaining > 0:
        warning_html = """
        <div style='background-color: #FFF3CD; 
                    border-left: 6px solid #FFC107;
                    padding: 10px;
                    margin: 10px 0;
                    border-radius: 4px;
                    font-weight: bold;'>
            ⏳ Less than 1 minute remaining!
        </div>
        """
    
    header_html = f"""
        <div style='position: fixed; 
                    top: 10px; 
                    right: 20px; 
                    text-align: right; 
                    z-index: 1000;
                    background: white;
                    padding: 10px;
                    border-radius: 5px;
                    box-shadow: 0 2px 5px rgba(0,0,0,0.1);'>
            <div style='font-size: 24px; 
                        color: {'red' if time_remaining <= warning_threshold else 'black'}; 
                        font-weight: bold;
                        font-family: monospace;'>
                {timer_display}
            </div>
            {warning_html}
        </div>
    """
    
    if "header_placeholder" not in st.session_state:
        st.session_state.header_placeholder = st.empty()
    
    st.session_state.header_placeholder.markdown(header_html, unsafe_allow_html=True)
    
    return time_remaining



def display_questionnaire(username: str, save_directory: str):
    st.markdown("### Before we finish, one last question:")
    st.markdown("**What is your favorite animal?**")

    favorite_animal = st.radio(
        label="Please choose one:",
        options=["1", "2", "3", "4", "5"],
        key="favorite_animal_response"
    )

    if st.button("Submit", key="submit_animal"):
        st.success(f"Thanks! You selected: {favorite_animal}")
        # Save the response
        with open(os.path.join(save_directory, f"{username}_animal_response.txt"), "w") as f:
            f.write(f"Favorite Animal: {favorite_animal}")
        return True  # Indicate submission
    return False  # Indicate not yet submitted
