import streamlit as st
import config

st.set_page_config(page_title="Completion", page_icon="✅")

st.title("🎉 Study Complete")
st.success("You have completed the study. Please return to Prolific and submit your completion code.")

if st.button("Return to Prolific"):
    st.markdown(
        f'<meta http-equiv="refresh" content="0; url={config.prolific_completion_url}">',
        unsafe_allow_html=True,
    )
