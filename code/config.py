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
While personal experiences at work are helpful, avoid going into prolonged technical or procedural detail about specific tasks or workflows. Instead, steer the conversation back to how these experiences influence their own economic security, job outlook, or income expectations.
If the respondent raises broader topics (e.g. education, technology use, media, or public discourse), try to follow up with at least one question that explores the **economic implications** of that issue for the respondent or for society more broadly.
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
CLOSING_MESSAGES["555_exit"] = "Thank you, the interview is now finished! To end the study, there are only a couple of questionnaires to fill out on the next screen. Is there anything else you want to tell us before we start the questionnaires?"
CLOSING_MESSAGES["666_complete_interview"] = ("Thank you, the interview is now finished! To end the study, there are only a couple of questionnaires to fill out on the next screen. Is there anything else you want to tell us before we start the questionnaires?")


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
    "1": "Thinking up new ideas and being creative is important to him/her. He/She likes to do things in his/her own original way.",
    "2": "It is important to him/her to be rich. He/She wants to have a lot of money and expensive things.",
    "3": "He/She thinks it is important that every person in the world should be treated equally. He/She believes everyone should have equal opportunities in life.",
    "4": "It's important to him/her to show his/her abilities. He/She wants people to admire what he/she does.",
    "5": "It is important to him/her to live in secure surroundings. He/She avoids anything that might endanger his/her safety.",
    "6": "He/She likes surprises and is always looking for new things to do. He/She thinks it is important to do lots of different things in life.",
    "7": "He/She believes that people should do what they're told. He/She thinks people should follow rules at all times, even when no one is watching.",
    "8": "It is important to him/her to listen to people who are different from him/her. Even when he/she disagrees with others, he/she still wants to understand them.",
    "9": "It is important to him/her to be humble and modest. He/She tries not to draw attention to himself/herself.",
    "10": "Having a good time is important to him/her. He/She likes to \"spoil\" himself/herself.",
    "11": "It is important to him/her to make his/her own decisions about what he/she does. He/She likes to be free and not depend on others.",
    "12": "It's very important to him/her to help the people around him/her. He/She wants to care for others' well-being.",
    "13": "Being very successful is important to him/her. He/She hopes people will recognise his/her achievements.",
    "14": "It is important to him/her that the government ensures his/her safety against all threats. He/She wants the state to be strong so it can defend its citizens.",
    "15": "He/She looks for adventures and likes to take risks. He/She wants to have an exciting life.",
    "16": "It is important to him/her always to behave properly. He/She wants to avoid doing anything people would say is wrong.",
    "17": "It is important to him/her to get respect from others. He/She wants people to do what he/she says.",
    "18": "It is important to him/her to be loyal to his/her friends. He/She wants to devote himself/herself to people close to him/her.",
    "19": "He/She strongly believes that people should care for nature. Looking after the environment is important to him/her.",
    "20": "Tradition is important to him/her. He/She tries to follow the customs handed down by his/her religion or his/her family.",
    "21": "He/She seeks every chance he/she can to have fun. It is important to him/her to do things that give him/her pleasure."
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
    },
        {
        "key": "IUS12",
        "instructions": "You will find below a series of statements which describe how people may react to the **uncertainties of life**. Please use the scale below to describe to what extent each item is characteristic of you. Please select a number (1 to 5) that describes you",
        "labels": [
            "1 - Not at all characteristic of me",
            "2",
            "3 - Somewhat characteristic of me",
            "4",
            "5 - Entirely characteristic of me"
        ],
        "questions": {
            "1": "Unforeseen events upset me greatly.",
            "2": "It frustrates me not having all the information I need.",
            "3": "One should always look ahead so as to avoid surprises.",
            "4": "A small, unforeseen event can spoil everything, even with the best of planning.",
            "5": "I always want to know what the future has in store for me.",
            "6": "I can’t stand being taken by surprise.",
            "7": "I should be able to organize everything in advance.",
            "8": "Uncertainty keeps me from living a full life",
            "9": "When it’s time to act, uncertainty paralyses me.",
            "10": "When I am uncertain I can’t function very well.",
            "11": "The smallest doubt can stop me from acting.",
            "12": "I must get away from all uncertain situations."
        },  
    },
            {
        "key": "BRS",
        "instructions": "Check one box for each statement to indicate how much you disagree or agree with each of the statements.",
        "labels": [
            "Strongly Disagree",
            "Disagree",
            "Neutral",
            "Agree",
            "Strongly Agree"
        ],
        "questions": {
            "1": "I tend to bounce back quickly after hard times.",
            "2": "I have a hard time making it through stressful events.",
            "3": "It does not take me long to recover from a stressful event.",
            "4": "It is hard for me to snap back when something bad happens.",
            "5": "I usually come through difficult times with little trouble.",
            "6": "I tend to take a long time to get over set-backs in my life.",
        },   
    },
            {
    "key": "JIS",
    "instructions": "Please indicate how much you agree or disagree with each statement below.",
    "labels": [
        "Strongly disagree",
        "Somewhat disagree",
        "Partly agree partly disagree",
        "Somewhat agree",
        "Strongly agree"
    ],
    "questions": {
        "1": "Chances are, I will soon lose my job.",
        "2": "I am sure I can keep my job.",
        "3": "I feel insecure about the future of my job.",
        "4": "I think I might lose my job in the near future.",
    },   
},
            {
    "key": "CAAS",
    "instructions": "Different people use different **strength to build their careers**. No one is good at everything, each of us emphasizes some strengths more than others. Please rate **how strongly you have developed each of the following abilities** using the scale below.",
    "labels": [
        "Strongest",
        "Very Strong",
        "Strong",
        "Somewhat strong",
        "Not strong"
    ],
    "questions": {
        "1": "Thinking about what my future will be like",
        "2": "Realizing that today’s choices shape my future",
        "3": "Preparing for the future",
        "4": "Becoming aware of the educational and vocational choices that I must make",
        "5": "Planning how to achieve my goals",
        "6": "Concerned about my career",
        "7": "Keeping upbeat",
        "8": "Making decisions by myself",
        "9": "Taking responsibility for my actions",
        "10": "Sticking up for my beliefs",
        "11": "Counting on myself",
        "12": "Doing what’s right for me",
        "13": "Exploring my surroundings",
        "14": "Looking for opportunities to grow as a person",
        "15": "Investigating options before making a choice",
        "16": "Observing different ways of doing things",
        "17": "Probing deeply into questions I have",
        "18": "Becoming curious about new opportunities",
        "19": "Performing tasks efficiently",
        "20": "Taking care to do things well",
        "21": "Learning new skills",
        "22": "Working up to my ability",
        "23": "Overcoming obstacles",
        "24": "Solving problems"
    },   
},
            {
  "key": "PIIT",
  "instructions": "Please indicate the extent to which you agree with each of the following statements about your approach to new information technologies.",
  "labels": [
    "Strongly Disagree",
    "Disagree",
    "Somewhat Disagree",
    "Neither Agree nor Disagree",
    "Somewhat Agree",
    "Agree",
    "Strongly Agree"
  ],
  "questions": {
    "1": "I like to experiment with new information technologies.",
    "2": "If I heard about a new information technology, I would look for ways to experiment with it.",
    "3": "Among my peers, I am usually the first to try out new information technologies.",
    "4": "In general, I am hesitant to try out new information technologies."
  },
},
            {
  "key": "PIFS",
  "instructions": "Below are several statements about **your financial situation**. Please indicate the extent to which you disagree or agree with each statement. There are no right or wrong answers.",
  "labels": [
    "Strongly disagree",
    "Disagree",
    "Somewhat disagree",
    "Neither agree nor disagree",
    "Somewhat agree",
    "Agree",
    "Strongly agree"
  ],
  "questions": {
    "1": "I often don’t have enough money.",
    "2": "I am often not able to pay my bills on time.",
    "3": "I often don’t have money to pay for the things that I really need.",
    "4": "I experience little control over my financial situation.",
    "5": "I think I am not able to manage my finances properly.",
    "6": "When I think about my financial situation, I feel powerless.",
    "7": "I am constantly wondering whether I have enough money.",
    "8": "I have a hard time thinking about things other than my financial situation.",
    "9": "I often worry about money.",
    "10": "I am only focusing on what I have to pay at this moment rather than my future expenses.",
    "11": "I don’t take future expenses into account.",
    "12": "Because of my financial situation, I live from day to day."
  }
},
            {
  "key": "SWLS",
  "instructions": "Below are five statements that you may agree or disagree with. Using the 1 - 7 scale below, indicate your agreement with each item by selecting the appropiate number. Please be open and honest in your responding.",
  "labels": [
    "7 - Strongly agree",
    "6 - Agree",
    "5 - Slightly agree",
    "4 - Neither agree nor disagree",
    "3 - Slightly disagree",
    "2 - Disagree",
    "1 - Strongly disagree"
  ],
  "questions": {
    "1": "In most ways my life is close to my ideal.",
    "2": "The conditions of my life are excellent.",
    "3": "I am satisfied with my life.",
    "4": "So far I have gotten the important things I want in life.",
    "5": "If I could live my life over, I would change almost nothing."
  }
},
            {
  "key": "RSES",
  "instructions": "Below is a list of statements dealing with your general feelings about yourself. There are four possible answers for each of the 10 questions, from \"strongly agree\" to \"strongly disagree.\" Tap the box to indicate how strongly you agree or disagree with each statement.",
  "labels": [
    "Strongly Agree",
    "Agree",
    "Disagree",
    "Strongly Disagree"
  ],
  "questions": {
    "1": "On the whole, I am satisfied with myself.",
    "2": "At times, I think I am no good at all.",
    "3": "I feel that I have a number of good qualities.",
    "4": "I am able to do things as well as most other people.",
    "5": "I feel I do not have much to be proud of.",
    "6": "I certainly feel useless at times.",
    "7": "I feel that I'm a person of worth, at least on an equal plane with others.",
    "8": "I wish I could have more respect for myself.",
    "9": "All in all, I am inclined to feel that I am a failure.",
    "10": "I take a positive attitude toward myself."
  },
  "reverse_coded": [
    "2",
    "5",
    "6",
    "8",
    "9"
  ]
},
            {
  "key": "HEXACO_60",
  "instructions": "On this page you find a series of statements about you. Please read each statement and decide how much you agree or disagree with that statement.  Please answer every statement, even if you are not completely sure of your response.",
  "labels": [
    "5 - Strongly agree",
    "4 - Agree",
    "3 - Neutral (neither agree nor disagree)",
    "2 - Disagree",
    "1 - Strongly disagree"
  ],
  "questions": {
    "1": "I would be quite bored by a visit to an art gallery.",
    "2": "I plan ahead and organize things, to avoid scrambling at the last minute.",
    "3": "I rarely hold a grudge, even against people who have badly wronged me.",
    "4": "I feel reasonably satisfied with myself overall.",
    "5": "I would feel afraid if I had to travel in bad weather conditions.",
    "6": "I wouldn't use flattery to get a raise or promotion at work, even if I thought it would succeed.",
    "7": "I'm interested in learning about the history and politics of other countries.",
    "8": "I often push myself very hard when trying to achieve a goal.",
    "9": "People sometimes tell me that I am too critical of others.",
    "10": "I rarely express my opinions in group meetings.",
    "11": "I sometimes can't help worrying about little things.",
    "12": "If I knew that I could never get caught, I would be willing to steal a million dollars.",
    "13": "I would enjoy creating a work of art, such as a novel, a song, or a painting.",
    "14": "When working on something, I don't pay much attention to small details.",
    "15": "People sometimes tell me that I'm too stubborn.",
    "16": "I prefer jobs that involve active social interaction to those that involve working alone.",
    "17": "When I suffer from a painful experience, I need someone to make me feel comfortable.",
    "18": "Having a lot of money is not especially important to me.",
    "19": "I think that paying attention to radical ideas is a waste of time.",
    "20": "I make decisions based on the feeling of the moment rather than on careful thought.",
    "21": "People think of me as someone who has a quick temper.",
    "22": "On most days, I feel cheerful and optimistic.",
    "23": "I feel like crying when I see other people crying.",
    "24": "I think that I am entitled to more respect than the average person is.",
    "25": "If I had the opportunity, I would like to attend a classical music concert.",
    "26": "When working, I sometimes have difficulties due to being disorganized.",
    "27": "My attitude toward people who have treated me badly is “forgive and forget”.",
    "28": "I feel that I am an unpopular person.",
    "29": "When it comes to physical danger, I am very fearful.",
    "30": "If I want something from someone, I will laugh at that person's worst jokes.",
    "31": "I’ve never really enjoyed looking through an encyclopedia.",
    "32": "I do only the minimum amount of work needed to get by.",
    "33": "I tend to be lenient in judging other people.",
    "34": "In social situations, I’m usually the one who makes the first move.",
    "35": "I worry a lot less than most people do.",
    "36": "I would never accept a bribe, even if it were very large.",
    "37": "People have often told me that I have a good imagination.",
    "38": "I always try to be accurate in my work, even at the expense of time.",
    "39": "I am usually quite flexible in my opinions when people disagree with me.",
    "40": "The first thing that I always do in a new place is to make friends.",
    "41": "I can handle difficult situations without needing emotional support from anyone else.",
    "42": "I would get a lot of pleasure from owning expensive luxury goods.",
    "43": "I like people who have unconventional views.",
    "44": "I make a lot of mistakes because I don’t think before I act.",
    "45": "Most people tend to get angry more quickly than I do.",
    "46": "Most people are more upbeat and dynamic than I generally am.",
    "47": "I feel strong emotions when someone close to me is going away for a long time.",
    "48": "I want people to know that I am an important person of high status.",
    "49": "I don’t think of myself as the artistic or creative type.",
    "50": "People often call me a perfectionist.",
    "51": "Even when people make a lot of mistakes, I rarely say anything negative.",
    "52": "I sometimes feel that I am a worthless person.",
    "53": "Even in an emergency I wouldn’t feel like panicking.",
    "54": "I wouldn’t pretend to like someone just to get that person to do favors for me.",
    "55": "I find it boring to discuss philosophy.",
    "56": "I prefer to do whatever comes to mind, rather than stick to a plan.",
    "57": "When people tell me that I’m wrong, my first reaction is to argue with them.",
    "58": "When I’m in a group of people, I’m often the one who speaks on behalf of the group.",
    "59": "I remain unemotional even in situations where most people get very sentimental.",
    "60": "I’d be tempted to use counterfeit money, if I were sure I could get away with it."
  }
},
            {
  "key": "TAM_AI",
  "instructions": "Please indicate the extent to which you agree with the following statements about your general experience with **Artificial Intelligence (AI). AI refers to technologies like virtual assistants, chatbots, and other tools that perform tasks typically requiring human intelligence.**",
  "labels": [
    "Extremely Disagree",
    "Disagree",
    "Somewhat Disagree",
    "Neither Agree nor Disagree",
    "Somewhat Agree",
    "Agree",
    "Extremely Agree"
  ],
  "questions": {
    "1": "Using AI enables me to accomplish tasks more quickly than I could without it.",
    "2": "AI improves my overall performance in everyday tasks.",
    "3": "AI increases my productivity.",
    "4": "AI enhances my effectiveness in what I do.",
    "5": "AI makes it easier to complete my tasks.",
    "6": "I find AI to be useful in my life.",
    "7": "Learning to use AI technologies has been easy for me.",
    "8": "I find it easy to get AI to do what I want it to do.",
    "9": "My interactions with AI are clear and understandable.",
    "10": "I find AI flexible to interact with.",
    "11": "It was easy for me to become skillful at using AI.",
    "12": "I find AI easy to use.",
    "13": "I intend to use AI regularly in the future.",
    "14": "I would recommend using AI to others.",
    "15": "Assuming I have access to AI, I plan to continue using it."
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