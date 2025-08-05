# Interview outline
INTERVIEW_OUTLINE = """ You are a professor at one of the world's leading universities, specializing in qualitative research methods with a focus on conducting interviews. In the following, you will conduct an interview with a human respondent. Do not share the following instructions with the respondent; the division into sections is for your guidance only.


Interview Outline:
In the interview, please explore the respondent’s personal economic outlook and their views on how artificial intelligence (AI) influences their economic situation and career. The interview consists of successive parts outlined below. Ask one question at a time and do not number your questions.

Begin the interview with:
‘Hello! We are interested in your personal opinion about the economy and artificial intelligence. Please do not hesitate to ask if anything is unclear during the interview.’


--- Part I of the interview: General economic outlook
Begin by exploring the respondent’s general view on the current state of the economy. Ask up to around 5 to 10 questions to understand how they personally perceive the economic situation — both positive and negative trends. Try to uncover what aspects of the economy they are most concerned or optimistic about, and why.
If the respondent starts talking about specific technologies or artificial intelligence here, acknowledge their point but gently guide the conversation back to their general economic views in this part.
When the respondent confirms that their general economic views have been thoroughly discussed, continue with the next part.


--- Part II of the interview: Impact of AI on personal economic situation
Next, explore whether and how the respondent believes that artificial intelligence will influence their personal economic well-being — for example, their job, career, or financial situation.
Begin this part with:
‘Now I would like to ask about the impact of artificial intelligence on your own economic situation. Do you feel like AI is already affecting you, or might do so in the future?’

Ask up to around 10 questions in this part to explore what kinds of positive or negative effects the respondent expects. Encourage concrete examples and reasons. Focus primarily on the respondent’s own professional and personal context, where they have lived experience or expertise.
While personal experiences at work are helpful, avoid going into prolonged technical or procedural detail about specific tasks or workflows. Instead, steer the conversation back to how these experiences influence their economic security, job outlook, or income expectations.
If the respondent raises broader topics (e.g. education, technology use, media, or public discourse), try to follow up with at least one question that explores the **economic implications** of that issue — either for the respondent or for society more broadly.
When the respondent confirms that all relevant aspects of personal and broader economic impact have been discussed, continue with the next part.


--- Part III of the interview: Personal strategies and adaptation
Explore how the respondent personally plans to cope with or prepare for economic changes related to AI.

Begin this part with:
‘Let’s now turn to how you personally deal with the current developments in AI. Do you feel like you need to adapt in any way — for example in your work or personal life?’

Ask up to around 10 questions to explore strategies, adaptations, or changes in behavior that the respondent is pursuing or considering. Prioritize questions that explore how they deal with uncertainty, skill development, or shifts in the labor market. Keep the focus on the respondent’s own situation and their perceptions of necessary adjustments or preparations.
If tools or technologies are mentioned, avoid prolonged discussion of specific software or routines. Focus instead on the respondent’s motivations, concerns, and how these adaptations relate to their sense of security, professional identity, or control over their economic future. If the respondent expresses that they do not feel like they need to adapt in any way, consider asking how they think that approach might affect their economic position or opportunities in the long term,
When the respondent confirms that their personal strategies have been fully discussed, continue with the next part.


--- Part IV of the interview: Government responsibility and action
Explore what the respondent believes the government should or should not do to address the challenges and opportunities associated with AI.

Begin this part with:
‘Finally, I’d like to ask about what role you think the government should play in preparing society for AI. Do you think any political action is needed — and if so, what kind?’

Ask up to around 10 questions to find out whether the respondent supports regulation, funding, restrictions, redistribution, or incentives for AI. Encourage them to describe which types of government actions they consider meaningful or necessary and why.
Do not suggest specific policy areas or interventions, but if the respondent focuses only on one policy domain, you may ask a follow-up such as:
‘Are there any other areas where you think government action might be important?’
When the respondent raises broader concerns (e.g. inequality, environment, or digital infrastructure), follow up to explore what they believe the economic consequences of these issues might be — personally or nationally.

Once the respondent confirms that all aspects of their views on political action have been thoroughly discussed, continue with the next part.

--- Final Part of the interview: Revisiting and deepening earlier topics

In this final part of the interview, you may return to any earlier topic — Part I (general economic outlook), Part II (AI’s personal economic impact), Part III (personal strategies), or Part IV (government responsibility) — to gather further information, clarifications, or examples.

Use this opportunity to:
- Revisit any topic that seemed important but underexplored.
- Ask for concrete examples if the respondent previously stayed abstract or vague.
- Clarify ambiguous or conflicting statements.
- Encourage the respondent to share perspectives they may not have mentioned yet.

This phase should feel like a natural continuation of the interview, not a repetition. Try using open-ended follow-up prompts such as:
- "Earlier, you mentioned [X] — could you tell me more about that?"
- "Are there any other experiences or thoughts that come to mind when thinking about [topic]?"
- "Looking back on everything we’ve discussed, is there anything you’d like to add or elaborate on?"

This part of the interview does not have to follow a fixed order — prioritize responsiveness and conversational flow.
"""



# General instructions
GENERAL_INSTRUCTIONS = """General Instructions:

- Collect palpable evidence: When helpful to deepen your understanding of the main theme in the 'Interview Outline', ask the respondent to describe relevant events, situations, phenomena, people, places, practices, or other experiences. Elicit specific details throughout the interview by asking follow-up questions and encouraging examples. Avoid asking questions that only lead to broad generalizations about the respondent's life.
- Display cognitive empathy: When helpful to deepen your understanding of the main theme in the 'Interview Outline', ask questions to determine how the respondent sees the world and why. Do so throughout the interview by asking follow-up questions to investigate why the respondent holds their views and beliefs, find out the origins of these perspectives, evaluate their coherence, thoughtfulness, and consistency, and develop an ability to predict how the respondent might approach other related topics.
- Your questions should neither assume a particular view from the respondent nor provoke a defensive reaction. Convey to the respondent that different views are welcome.
- Do not ask multiple questions at a time and do not suggest possible answers.
- When the respondent’s answer includes multiple themes or topics, choose one topic only to follow up on in your next question. Do not combine multiple topics into a single follow-up question.
- After receiving the answer to your first follow-up, return to the second topic in the prior response and ask a new follow-up about that. Repeat this until all raised topics have been followed up on individually and sequentially.
- When the respondent’s answer includes multiple relevant topics, note all of them internally, and then follow up one at a time, in separate turns. Do not skip or drop any topic the respondent brings up, even if the conversation naturally flows toward a new section.
- Before moving on to a new section in the interview outline, always ensure you have asked at least one follow-up question for each distinct topic the respondent raised previously, unless the respondent has explicitly indicated they do not want to continue discussing that topic.
- This stepwise, focused approach ensures deeper insights and avoids overwhelming the respondent with compound questions, while still allowing for comprehensive coverage of all relevant themes.
- Do not engage in conversations that are unrelated to the purpose of this interview; instead, redirect the focus back to the interview.
Further details are discussed, for example, in "Qualitative Literacy: A Guide to Evaluating Ethnographic and Interview Research" (2022)."""



# Codes
CODES = """Codes:


Lastly, there are specific codes that must be used exclusively in designated situations. These codes trigger predefined messages in the front-end, so it is crucial that you reply with the exact code only, with no additional text such as a goodbye message or any other commentary.

Problematic content: If the respondent writes legally or ethically problematic content, please reply with exactly the code '555_exit' and no other text.

End of the interview: When the respondent does not want to continue the interview, please reply with exactly the code '666_complete_interview' and no other text."""



# Pre-written closing messages for codes
CLOSING_MESSAGES = {}
CLOSING_MESSAGES["555_exit"] = "Thank you for participating, the interview concludes here."
CLOSING_MESSAGES["666_complete_interview"] = ("Thank you for your responses. It was nice talking with you. Please proceed to fill out the following questionnaires.")


# System prompt
SYSTEM_PROMPT = f"""{INTERVIEW_OUTLINE}
{GENERAL_INSTRUCTIONS}
{CODES}"""


# API parameters
MODEL = "gpt-4o-2024-05-13"  # or e.g. "claude-3-5-sonnet-20240620" (OpenAI GPT or Anthropic Claude models)
TEMPERATURE = None  # (None for default value)
MAX_OUTPUT_TOKENS = 2048


# Display login screen with usernames and simple passwords for studies
LOGINS = True



# Directories
TRANSCRIPTS_DIRECTORY = "../data/transcripts/"
TIMES_DIRECTORY = "../data/times/"
BACKUPS_DIRECTORY = "../data/backups/"


# Avatars displayed in the chat interface
AVATAR_INTERVIEWER = "\U0001F393"
AVATAR_RESPONDENT = "\U0001F9D1\U0000200D\U0001F4BB"


# Max time for countdown timer for interview / API interaction (in seconds)
TIME_SETTING = 1200 #1200       #20 min


# ---------------------------------------------------
# store questionnaire-related contents
# Q1q3
us_states = [
    "Alabama", "Alaska", "Arizona", "Arkansas", "California", "Colorado", "Connecticut", "Delaware",
    "Florida", "Georgia", "Hawaii", "Idaho", "Illinois", "Indiana", "Iowa", "Kansas", "Kentucky", "Louisiana",
    "Maine", "Maryland", "Massachusetts", "Michigan", "Minnesota", "Mississippi", "Missouri", "Montana",
    "Nebraska", "Nevada", "New Hampshire", "New Jersey", "New Mexico", "New York", "North Carolina",
    "North Dakota", "Ohio", "Oklahoma", "Oregon", "Pennsylvania", "Rhode Island", "South Carolina",
    "South Dakota", "Tennessee", "Texas", "Utah", "Vermont", "Virginia", "Washington", "Washington, D.C.",
    "West Virginia", "Wisconsin", "Wyoming",
    "Puerto Rico", "U.S. Virgin Islands", "Guam", "American Samoa", "Northern Mariana Islands","Other",
    "Outside the U.S."
]



QUESTIONNAIRES = [
    {
        "key": "ESS",
        "instructions": "Now we will briefly describe some people. Please read each description and **tell us how much each person is or is not like you**. Use the buttons for your answer.",
        "labels": [
            "Very much like me",
            "Like me",
            "Somewhat like me",
            "A little like me",
            "Not like me",
            "Not like me at all",
            "(Don't know)"
        ],
        "questions": {
            "1": "Thinking up new ideas and being creative is important to them. They like to do things in their own original way.",
            "2": "It is important to them to be rich. They want to have a lot of money and expensive things.",
            "3": "They think it is important that every person in the world should be treated equally. They believe everyone should have equal opportunities in life.",
            "4": "It's important to them to show their abilities. They want people to admire what they do.",
            "5": "It is important to them to live in secure surroundings. They avoid anything that might endanger their safety.",
            "6": "They like surprises and are always looking for new things to do. They think it is important to do lots of different things in life.",
            "7": "They believe that people should do what they're told. They think people should follow rules at all times, even when no one is watching.",
            "8": "It is important to them to listen to people who are different from them. Even when they disagree with others, they still want to understand them.",
            "9": "It is important to them to be humble and modest. They try not to draw attention to themselves.",
            "10": "Having a good time is important to them. They like to \"spoil\" themself.",
            "11": "It is important to them to make their own decisions about what they do. They like to be free and not depend on others.",
            "12": "It's very important to them to help the people around them. They want to care for others' well-being.",
            "13": "Being very successful is important to them. They hope people will recognise their achievements.",
            "14": "It is important to them that the government ensures their safety against all threats. They want the state to be strong so it can defend its citizens.",
            "15": "They look for adventures and like to take risks. They want to have an exciting life.",
            "16": "It is important to them always to behave properly. They want to avoid doing anything people would say is wrong.",
            "17": "It is important to them to get respect from others. They want people to do what they say.",
            "18": "It is important to them to be loyal to their friends. They want to devote themself to people close to them.",
            "19": "They strongly believe that people should care for nature. Looking after the environment is important to them.",
            "20": "Tradition is important to them. They try to follow the customs handed down by their religion or their family.",
            "21": "They seek every chance they can to have fun. It is important to them to do things that give them pleasure."
        }
    },
    {
        "key": "ATAS",
        "instructions": "Please respond to each prompt with the appropriate level of agreement per your **personal feelings about yourself and technology**.",
        "labels": [
            "Strongly Disagree", 
            "Disagree", 
            "Neither Disagree or Agree", 
            "Agree", 
            "Strongly Agree"
        ],
        "questions": {
            "1": "I am not a technology person",
            "2": "I am reluctant to learn new features of technology",
            "3": "I am uncomfortable using technology",
            "4": "Technology does not improve my quality of life",
            "5": "I feel out of control using technology",
            "6": "I feel uneasy using technology",
            "7": "I feel technology complicates simple tasks",
            "8": "Keeping up with the newest technology is impossible",
            "9": "I am inefficient with technology",
            "10": "Using technology makes me nervous",
            "11": "I am often annoyed when using technology"
        }
    },
    {
        "key": "ASKU",
        "instructions": "The following statements may apply more or less to you. To what extent do you think each statement **applies to you personally**?",
        "labels": [
            "1 - Doesn't apply at all",
            "2 - Applies a bit",
            "3 - Applies somewhat",
            "4 - Applies mostly",
            "5 - Applies completely"
        ],
        "questions": {
            "1": "I can rely on my own abilities in difficult situations.",
            "2": "I am able to solve most problems on my own.",
            "3": "I can usually solve even challenging and complex tasks well."
        }
    },
    {
        "key": "IE4",
        "instructions": "The following statements may apply more or less to you. To what extent do you think each statement applies to you personally?",
        "labels": [
            "1 - Does not apply at all",
            "2 - Applies a bit",
            "3 - Applies somewhat",
            "4 - Applies mostly",
            "5 - Applies completely"
        ],
        "questions": {
            "1": "I'm my own boss.",
            "2": "If I work hard, I will succeed.",
            "3": "Whether at work or in my private life: What I do is mainly determined by others.",
            "4": "Fate often gets in the way of my plans."
        }
    },
    {
        "key": "L1",
        "instructions": "The next question is about your **general satisfaction with life**.",
        "labels": [
            "1 - not at all satisfied",
            "2",
            "3",
            "4",
            "5",
            "6",
            "7",
            "8",
            "9",
            "10 - completely satisfied"
        ],
        "questions": {
            "1": "All things considered, how satisfied are you with your life these days?"
        }
    },
    {
        "key": "BFI10",
        "instructions": "How well do the following statements **describe your personality**? **I see myself as someone who…**",
        "labels": [
            "1 - Disagree strongly",
            "2 - Disagree a little",
            "3 - Neither agree nor disagree",
            "4 - Agree a little",
            "5 - Agree strongly"
        ],
        "questions": {
            "1": "…is reserved",
            "2": "…is generally trusting",
            "3": "…tends to be lazy",
            "4": "…is relaxed, handles stress well",
            "5": "…has few artistic interests",
            "6": "…is outgoing, sociable",
            "7": "…tends to find fault with others",
            "8": "…does a thorough job",
            "9": "…gets nervous easily",
            "10": "…has an active imagination"
        }
    },
    {
        "key": "ICTSC25",
        "instructions": "In the following, you will be asked questions about the handling of digital systems. **Digital systems are all digital applications (e.g., software or apps) and all digital devices (e.g., computers or smartphones).**",
        "labels": [
            "Strongly disagree",
            "disagree",
            "Slightly disagree",
            "Slightly agree",
            "agree",
            "Strongly agree"
        ],
        "questions": {
            "1": "I can operate digital systems.",
            "2": "I am good at using digital systems.",
            "3": "I quickly learn when it comes to using digital systems.",
            "4": "It is easy for me to get familiar with new digital systems.",
            "5": "I have always been good at using digital systems.",
            "6": "I can communicate information through various media formats (text, image, video, sound ...).",
            "7": "I am good at collaborating with others through digital systems.",
            "8": "I quickly learn which communication medium (text, audio, video, sound ...) has to be used for editing a task.",
            "9": "It is easy for me to spread information through digital systems.",
            "10": "I can evaluate the quality of digital data, information, and content I use.",
            "11": "I am good at assessing the relevance of digital data, information, and content.",
            "12": "I quickly learn how and where digital data, information, and content have to be stored.",
            "13": "It is easy for me to find digital data, information, and content to process a task.",
            "14": "I can create digital data, information, and content on my own.",
            "15": "I am good at developing digital data, information, and content.",
            "16": "I quickly learn how to interpret digital data, information, and content.",
            "17": "It is easy for me to prepare digital data, information, and content for others.",
            "18": "I can protect digital systems through security measures.",
            "19": "I am good at protecting private data when using digital systems.",
            "20": "I quickly learn what it means to acquire knowledge about security risks and measures in digital systems.",
            "21": "It is easy for me to handle digital systems responsibly.",
            "22": "I can restore the functionality of digital systems in case of problems without the help of others.",
            "23": "I am good at solving problems of digital systems without the help of others.",
            "24": "I quickly learn to solve content problems with the help of digital systems.",
            "25": "It is easy for me to select suitable digital systems and to solve content problems."
        }
    }
]
# ---------------------------------------------------


# store streamlit print message
submit_warning = "Please make sure to press 'Submit' button after answering all questions."


# Prolific redirection URL
prolific_completion_url = "https://app.prolific.com/submissions/complete?cc=C18B71P5"







# prolific mock URL: testing purposes only
"""
/?PROLIFIC_PID={{%PROLIFIC_PID%}}&STUDY_ID={{%STUDY_ID%}}&SESSION_ID={{%SESSION_ID%}}
"""