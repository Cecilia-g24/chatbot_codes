# interview.py (landing page)

import streamlit as st
#from streamlit_extras.switch_page_button import switch_page
from utils import (
    check_password,
    check_if_interview_completed,
    save_interview_data,
    check_prolific_access
)
import os
import config



st.set_page_config(page_title="Interview Start", page_icon="💬")
# Test switch (True = test mode with password login, False = Prolific mode)
st.session_state.test_Mode = True

# Extract Prolific parameters from URL 
prolific_pid = st.query_params.get("PROLIFIC_PID")
prolific_pid = prolific_pid[0] if isinstance(prolific_pid, list) and prolific_pid else prolific_pid
prolific_pid = prolific_pid if isinstance(prolific_pid, str) and prolific_pid else None
# on-screen display to show prolific id
#if prolific_pid:
#   st.markdown(f"👤 Prolific PID: `{prolific_pid}`")

# Auth vs. Prolific mode
if config.LOGINS:
    pwd_correct, username = check_password()
    if not pwd_correct:
        st.stop()
    st.session_state.username = username
else:
    st.session_state.username = prolific_pid
    check_prolific_access()

st.title("Important Information for Participants")

st.markdown("""
Thank you for your interest in our study. This is a **non-commercial research project** conducted by the Nuremberg Institute for Market Decisions (NIM), a non-profit organization. The purpose of the study is to better understand what people think about the economy and the role of artificial intelligence (AI) in their lives.

This study is conducted for scientific, non-commercial purposes. In addition to academic publications, some of the research results will be made available to the public. Your participation in this study is completely voluntary. You have to be at least 18 years old to take part. The whole study takes about 1 hour. 
""")

st.header("What does the study involve?")

st.subheader("Chatbot Interview")
st.markdown("""
In the first part, you will engage in a text-based conversation with a chatbot for about 30 minutes. The chatbot will ask questions about your personal opinions and experiences related to the economy and artificial intelligence.
- You do **not** need to have any special knowledge.
- **All views are welcome.**
- You decide which experiences or thoughts you want to share with us.
""")

st.subheader("Questionnaires")
st.markdown("""
After the interview, you will be asked to complete a set of questionnaires for about 30 minutes. These include:

- Basic demographic information (e.g., age, gender, education)
- Standardized psychological and personality questionnaires
""")

st.header("Important Information About Your Privacy and Data Use")

st.markdown("""
Your privacy and confidentiality are extremely important to us. To help protect your identity:

- Do **not** share any personally identifiable information during the chatbot interview. This includes names, addresses, phone numbers, email addresses, employer names, or any other details that could identify you or someone else.
- Do **not** disclose confidential or sensitive information that you or others would prefer to keep private.
- Only share information you would feel comfortable posting in a public forum.

We will attempt to detect and remove personally identifiable information from the data stored at NIM before data analysis, but we **cannot guarantee** complete removal. **You are responsible for what you choose to share.**
""")

st.subheader("Use of the OpenAI API")
st.markdown("""
- The chatbot interview (but not any other part of this study)  uses technology developed by OpenAI, Inc., a U.S.-based company. This technology enables a  realistic and interactive conversation experience. From a technical perspective, the interview is conducted via the OpenAI API, which means that your inputs during the conversation are transmitted to OpenAI's servers, where they are processed in real time to generate appropriate responses.
- NIM does **not** control how OpenAI stores or processes interview responses.
- If you are uncomfortable with OpenAI processing your interview responses, **please do not participate**.
""")

st.subheader("Data Storage and Use")
st.markdown("""
- Your interview and questionnaire data will be stored securely by NIM.
- Data stored by the NIM is used solely for **scientific, non-commercial** research.
- Any results shared will be **fully anonymized**.
""")



st.markdown("""
The survey is conducted by the Nürnberg Institut für Marktentscheidungen e.V., Steinstr. 21, 90419 Nürnberg, Germany (Nuremberg Institute for Market Decisions – “NIM”). You will find information about the collection, processing, and protection of your Personal Information (defined below), including the rights to which you are entitled, below.
""")

st.header("Privacy Statement")
st.markdown("""
Within the scope of the study, importance is given to compliance with U.S. Data Privacy Laws as well as the confidentiality of Personal Information. We strictly adhere to all laws and regulations on data protection applicable to residents of the United States of America, including, without limitation, the California Consumer Privacy Act (as amended by the California Privacy Rights Act), the Colorado Privacy Act, the Connecticut Personal Data Privacy and Online Monitoring Act, Nevada’s Senate Bill 2020, the Utah Consumer Privacy Act, and the Virginia Consumer Data Protection Act (collectively, as may be amended from time to time, „U.S. Data Privacy Laws“). With this privacy statement, we inform you about the collection and processing of your Personal Information and the rights to which you are entitled.
""")

st.header("Business")
st.markdown("""
Nürnberg Institut für Marktentscheidungen e.V., Steinstrasse 21, 90419 Nürnberg, Germany. 
Tel. +49 911 9 51 51 983
Fax +49 911 37677 872
hello@nim.org
""")

st.header("Data Protection Officer")
st.markdown("""
If you have any questions for our Data Protection Officer about the protection of your Personal Information, please email us at privacy@nim.org. Alternatively, you can also send your request tot he above address („Business“).
""")

st.header("Scope of information processing")
st.markdown("""
The information you provide to us during the study, which may include demographic information like age, gender, financial situation and your self-written interview responses and any other information that may identify, relate to, describe, or which is reasonably capable of being associated with, or could reasonably be linked, directly or indirectly, with you or your household (collectively, “Personal Information”), will be processed by NIM exclusively for the purpose of this study and potential follow-up studies for related non-commercial research. Pursuant to U.S. Data Privacy Laws, the legal basis for the processing of your Personal Information is your consent.
Except as expressly stated in this privacy statement, Personal Information collected in the course of the survey will not be disclosed to any other third parties unless we are expressly obliged to do so by law. Personal Information will be collected, processed, and stored exclusively within the European Union. When you provide Personal Information to us, you consent to the processing and storage of your Personal Information in the European Union.
Personal Information is deleted once the purpose for which it was collected no longer applies and in accordance with the retention and deletion periods required by U.S. Data Privacy Laws.
If you participate in the survey via Prolific you need to have a valid Prolific account. Furthermore, Prolifc collects certain technical data, including your Submission ID, Participant ID and timestamp, and your inputs (collectively, “Usage Data”), is automatically collected by the servers of Prolific. We use reasonable efforts to engage service providers that take appropriate measures to protect your Personal Information; however, it is the responsibility of each of those service providers to comply with U.S. Data Privacy Laws, and we take no responsibility for their privacy practices and compliance. For further details, please refer to the privacy policy of the service provider: https://prolific.notion.site/Privacy-Notices-2d794a61037642daaa4717e0944a8588.
            
We use the OpenAI API for the text-based interview in this study. OpenAI collects certain technical data, including time stamps, and your inputs (collectively, “Usage Data”) during the interview section of this study. Please note: If you exercise your right to deletion, we can erase the data we have stored, provided that no statutory retention obligations prevent deletion. However, we have no control over data processed and possibly temporarily stored by OpenAI during the chatbot interaction. According to OpenAI’s current data policy, such data is generally deleted after 30 days; changes to this policy are, however, out of our control. We use reasonable efforts to engage service providers that take appropriate measures to protect your Personal Information; however, it is the responsibility of each of those service providers to comply with U.S. Data Privacy Laws, and we take no responsibility for their privacy practices and compliance. For further details, please refer to the privacy policy of the service provider: https://platform.openai.com/docs/guides/your-data 
""")

st.header("Voluntary Participation and Consent")

st.markdown("""
By participating, you confirm that:

- You are at lest 18 years old.
- You understand the purpose and structure of the study.
- You understand the risks related to sharing personal information.
- You consent to the processing your interview responses via the OpenAI API.
- You consent to anonymized data use for scientific research and related publications.

If you do **not** agree with any part, **please do not continue**.
""")

# Consent checkbox
agree1 = st.checkbox("I hereby consent that the information provided by me within the survey, some of which may constitute „Personal Information“ as such term is used under U.S. Data Privacy Laws (defined above), may be collected and processed by NIM and disclosed by NIM to its third-party external research partners for the purpose of evaluating the survey. I am aware that I can withdraw my consent at any time by contacting NIM’s Data Protection Officer at privacy@nim.org. The withdrawl of consent does not affect the lawfulness of the processing carried out on the basis oft the consent until the withdrawal.")

agree2 = st.checkbox("I confirm that I have read and understood the information above. I voluntarily agree to take part in this study under the conditions described.")

if agree1 and agree2:
    st.success("✅ Thank you for consenting! You can now start the interview.")
    st.session_state["consent_given"] = True
    if st.button("▶️ Start Interview"):
        st.switch_page("pages/chatbot.py")
else:
    st.warning("Please confirm your consent to continue.")

