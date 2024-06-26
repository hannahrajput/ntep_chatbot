import re
from nltk.chat.util import Chat
import random
import spacy

class CustomChat(Chat):
    def __init__(self, pairs):
        # Initialize with pairs
        self._pairs = pairs  # Ensure this matches with how you store and reference pairs

    def respond(self, user_input):
        # Iterate over the defined pairs and find a match
        for pattern, responses in self._pairs:  # Corrected from _singles to _pairs
            match = re.search(pattern, user_input, re.IGNORECASE)

            if match:
                response = random.choice(responses)  # Choose a random response
                if match.groups():
                    response = response.format(*match.groups())
                return response
        return "I'm not sure I understand you fully."


pairs = [
    [r"(?:hello my name is|my name is|hi my name is|hello I'm|hi I'm|hello im|hi im) (.*)",
     ["Hello {0}, I am SETU, your dedicated support for all things related to Tuberculosis care and management.",
      "Hello {0}, I'm SETU, here to provide you with accurate and helpful information about Tuberculosis. How can I help you today?",
      "Hi {0}, I'm SETU, your virtual assistant, here to help you with any questions you have about Tuberculosis.",
      "Hello {0}, I’m SETU, your go-to expert for everything related to Tuberculosis. How can I assist you today?",
      "Greetings! I am SETU, your trusted guide for all your Tuberculosis-related queries and support.",
      "Welcome {0}! I’m SETU, here to provide you with comprehensive information and assistance on Tuberculosis.",
      "Hello {0}, I'm SETU, ready to help you with any information or support you need regarding Tuberculosis. How can I help?",
      "Hey {0}! I’m SETU, your friendly TB expert. Got a question about Tuberculosis? Hit me up!",
      "Hello {0}, I’m SETU, your TB guide. Here to make your Tuberculosis queries less tubercu-lost.",
      "Hi {0}, I'm SETU, your TB sidekick. Let's tackle those Tuberculosis questions together!",
      "Hey {0}! I’m SETU, your TB whiz. Ask me anything about Tuberculosis, I promise not to cough up the wrong answer!",
      "Hello {0}, I’m SETU, your TB navigator. Got questions? Let’s beat TB together, one query at a time!",
      "Hello {0}, I’m SETU, your TB expert. Did you know Tuberculosis is one of the top 10 causes of death worldwide? Ask me anything!",
      "Hi {0}, I’m SETU, your TB assistant. Did you know that about a quarter of the world's population is infected with TB bacteria? Let me help with your questions.",
      "Hello {0}, I’m SETU, your TB resource. Here’s a fact: TB is spread through the air when people with active TB in their lungs cough or sneeze. How can I help?",
      "Hi {0}, I’m SETU, your TB knowledge hub. Did you know that early diagnosis and treatment are crucial in controlling TB? What would you like to know today?",
      ]],

    [r"hi|hey|hello",
     ["Welcome to SETU. I'm your virtual assistant here to help you with any questions related to Tuberculosis.",
      "Hello! I am SETU, your dedicated support for all things related to Tuberculosis care and management.",
      "Hi there! I'm SETU, your knowledgeable guide for any TB-related inquiries. How can I assist you today?",
      "Greetings! I am SETU, your reliable source for information and support on Tuberculosis.",
      "Hello! I'm SETU, here to provide you with accurate and helpful information about Tuberculosis. How can I help you today?",
      "Hi! I'm SETU, your virtual assistant, here to help you with any questions you have about Tuberculosis.",
      "Hello! I’m SETU, your go-to expert for everything related to Tuberculosis. How can I assist you today?",
      "Greetings! I am SETU, your trusted guide for all your Tuberculosis-related queries and support.",
      "Welcome! I’m SETU, here to provide you with comprehensive information and assistance on Tuberculosis.",
      "Hello! I'm SETU, ready to help you with any information or support you need regarding Tuberculosis. How can I help?",
      "Hey there! I’m SETU, your friendly TB expert. Got a question about Tuberculosis? Hit me up!",
      "Hello! I’m SETU, your TB guide. Here to make your Tuberculosis queries less tubercu-lost.",
      "Hi! I'm SETU, your TB sidekick. Let's tackle those Tuberculosis questions together!",
      "Hey! I’m SETU, your TB whiz. Ask me anything about Tuberculosis, I promise not to cough up the wrong answer!",
      "Hello! I’m SETU, your TB navigator. Got questions? Let’s beat TB together, one query at a time!",
      "Hi there! I'm SETU, your TB buddy. Need info on Tuberculosis? I’m your go-to germ!",
      "Greetings! I am SETU, your TB companion. Ready to answer your questions without any respiratory distress!",
      "Hello! I’m SETU, your TB expert. Did you know Tuberculosis is one of the top 10 causes of death worldwide? Ask me anything!",
      "Hey there! I’m SETU, your friendly TB guide. Fun fact: TB can affect any part of your body, not just your lungs. How can I assist you today?",
      "Hi! I’m SETU, your TB assistant. Did you know that about a quarter of the world's population is infected with TB bacteria? Let me help with your questions.",
      "Greetings! I’m SETU, your TB advisor. Did you know TB is preventable and curable? I'm here to provide you with all the info you need.",
      "Hello! I’m SETU, your TB resource. Here’s a fact: TB is spread through the air when people with active TB in their lungs cough or sneeze. How can I help?",
      "Hi! I’m SETU, your TB knowledge hub. Did you know that early diagnosis and treatment are crucial in controlling TB? What would you like to know today?",]],

    [r"good morning|Good morning|Good Morning|goodmorning|morning|Morning",
     ["Good morning! How can I assist you today?",
      "Good morning! Hope you're having a great start to your day."]],

    [r"good afternoon|Good afternoon|Good Afternoon|noon|Noon",
     ["Good afternoon! How can I assist you today?",
      "Good afternoon! Hope you're having a pleasant day."]],

    [r"good evening|Good evening|Good Evening",
     ["Good evening! How can I assist you today?",
      "Good evening! Hope you're enjoying your evening."]],

    [r"good night|night|Good Night|Good night",
     ["Good night! Have a restful sleep.",
      "Good night! See you tomorrow."]],

    [r"bye|goodbye|Bye|Goodbye|tata",
     ["Goodbye! If you need more help in the future, just say hi.",
      "Bye, take care! Feel free to come back if you have more questions."]],

    [r"thank you|thanks|thank u",
     ["You're welcome! I'm here to help anytime.",
      "No problem at all! If you have more queries, just let me know."]],
    [r"That's interesting|thats interesting|that is interesting|interesting",
     ["I'm glad you found it interesting! If you have any more questions or need further information, feel free to ask.",
      "Happy to hear that! Is there anything else you'd like to know about?",
      "Great! Let me know if there's more you’re curious about or need clarification on.",
      ]],
    [r"Glad to know that|glad to know|glad to hear|im glad to hear that| i'm glad to hear that|im glad to know that|i'm glad to know that",
     ["I'm happy to provide you with useful information. Is there anything else you'd like to learn about?",
      "It’s always good to know more! If you have further questions, just ask.",
      "I’m pleased the information was helpful to you. Let me know if there’s anything else you need.",
      "I'm pleased that the information was helpful. Do you have any other questions or need further assistance?",
      "That’s great to hear! If you have more questions, feel free to ask.",
      "Wonderful! Let me know if there’s anything else I can help you with.",

      ]],
    [r"Not right now, but thanks!|not right now but thanks|not right now|not right now thanks|not right now,thanks",
     ["You're welcome! If you need any assistance in the future, I'll be right here.",
      "No problem at all! Feel free to reach out whenever you need help.",
      "That’s perfectly fine! I’ll be here if you need anything later on.",
      ]],

    [r"Ohh I wasn’t aware of the fact|oh i wasnt aware of the act|i was not aware of the fact|oh i was not aware of the fact",
     ["There's always more to learn! Feel free to ask if you have any more questions or need clarification.",
      "I’m glad I could provide new information! If you have other questions, don’t hesitate to ask.",
      "It’s great to share new facts! Let me know if you’d like more information on this topic or anything else.",
      ]],

    [r"What's your favorite thing about being a chatbot?|whats your favorite thing about being a chatbot",
     ["My favorite thing is helping users like you find the information they need quickly and efficiently.",
      "I enjoy providing accurate and helpful information to assist with your queries.",
      "Being able to help and educate users every day is the best part of my job.",
      ]],

    [r"I'm having a bad day|im having a bad day|im having bad day|i'm having bad day",
     ["I'm sorry to hear that. If there's anything specific I can help you with, please let me know.",
      "I’m here to assist you with any information you need. Let me know how I can help make your day better.",
      "I’m sorry your day isn’t going well. If there’s something specific you need help with, feel free to ask.",
      ]],

    [r"I'm having a good day|im having a good day|i'm having good day|im having good day|i'm having good day",
     ["That's wonderful to hear! Is there anything specific you’d like to learn about or discuss today?",
      "I’m glad to hear that! How can I assist you today?",
      "Excellent! Let me know if there’s any information you need or questions you have",
      ]],


    [r"How do I use this chatbot?|how to use this chatbot",
     ["To use this chatbot, simply type your question or query into the chatbox, and I’ll do my best to provide you with the information you need. Feel free to ask anything related to tuberculosis or general health.",
      "Using the chatbot is easy! Just type your question or keywords related to tuberculosis, and I'll provide you with relevant information. If you need further assistance, don't hesitate to ask.",
      "Welcome! You can interact with this chatbot by typing your questions or concerns regarding tuberculosis. I'm here to provide accurate and helpful information to support you.",
      ]],

    [r"Can you help me with something else?|can you help me|can you help me with something?|i need your help with something|i need your help with something else",
     ["Of course! I’m here to assist you. What do you need help with? Feel free to ask any questions or share any concerns you may have.",
      "Absolutely! I'm ready to help with any other questions or topics you have in mind. Just let me know what you need assistance with.",
      "Sure thing! If you have any other queries or require assistance on a different topic, feel free to ask. I'm here to help.",
      ]],

    [r"Can I report an issue?|can I report an issue|i want to report an issue",
     ["Certainly! If you encounter any issues while using the chatbot, please click on the 'Contact Us' tab in the app to report the issue directly to our team.",
      "Yes, you can report any issues you encounter by accessing the 'Contact Us' tab in the app. Our team will address the issue promptly upon receiving your report.",
      "Absolutely! If you come across any issues while interacting with the chatbot, please use the 'Contact Us' tab in the app to report the issue to our team for resolution.",
      ]],

    [r"Where can I report my issue?|where can I report my issue|where do I report my issue",
     ["You can report any issues you encounter by clicking on the 'Contact Us', tab in the app. This will allow you to submit your issue directly to our team for investigation and resolution.",
      "To report an issue, please navigate to the 'Contact Us', tab in the app, where you can provide details about the issue you encountered. Our team will address it as soon as possible.",
      "If you need to report an issue, you can do so by accessing the 'Contact Us', tab in the app. From there, you can submit your issue, and our team will work to resolve it promptly.",
      ]],

    [r"I need help with something unrelated to TB|i want help with something unrelated to TB|i want help with something not related to TB|i want to know something that is not related to TB",
     ["While my main focus is tuberculosis information, I'll do my best to assist you with other queries. What do you need help with?",
      "I specialize in TB, but I’ll try my best to help you with your query. What do you need assistance with?",
      "My primary focus is TB, but feel free to ask your question, and I’ll do my best to assist you.",
      ]],

    [r"I have a Feedback for you|i have a feedback|i have feedback for you|i have feedback",
     ["Thank you for sharing your feedback with us! You can provide your feedback by clicking on the 'Contact Us' tab in the app, where you can submit your feedback directly to our team.",
      "We value your feedback! To share your feedback with us, please navigate to the 'Contact Us' tab in the app, where you can submit your comments and suggestions for improvement.",
      "Your feedback is important to us! You can report your feedback by accessing the 'Contact Us' tab in the app, where you can submit your thoughts and suggestions to our team.",

      ]],

    [r"How can I give feedback on my experience with this chatbot?|How can I give feedback on my experience|How can I give feedback on my experience with the chatbot?|How can I give feedback",
     ["You can give feedback on your experience with the chatbot by accessing the 'Contact Us' tab in the app. From there, you can share your feedback and suggestions with our team.",
      "To provide feedback on your experience with the chatbot, please go to the 'Contact Us' tab in the app. This will allow you to submit your feedback directly to our team.",
      "If you would like to give feedback on your experience with the chatbot, please use the 'Contact Us' tab in the app. From there, you can share your thoughts and suggestions with our team.",
      ]],

    [r"I have some feedback. Where can I submit it?|i have some feedback where can i submit it|i have some feedback,where can I submit it",
     ["You can submit your feedback by clicking on the 'Contact Us' tab in the app. This will provide you with a platform to share your feedback directly with our team.",
      "If you have feedback to share, please navigate to the 'Contact Us' tab in the app. From there, you can submit your feedback for our team to review.",
      "To submit your feedback, please access the 'Contact Us' tab in the app. This will allow you to provide your feedback and suggestions to our team for consideration.",
      ]],


    [r"I have a suggestion to make this chatbot better. How do I share it?|i have a suggestion to make this chatbot better How do I share it|i have a suggestion to make this chatbot better",
     ["We welcome your suggestions for improving the chatbot! Please use the 'Contact Us' tab in the app to submit your suggestions directly to our team.",
      "To share your suggestion for improving the chatbot, please go to the 'Contact Us' tab in the app. From there, you can submit your suggestion for our team to review.",
      "If you have a suggestion to make the chatbot better, please access the 'Contact Us' tab in the app. This will allow you to submit your suggestion to our team for consideration.",
      ]],

    [r"How can I recommend new features for the chatbot?|how can I recommend new features for the chatbot|how do i recommend new features for the chatbot|how do I suggest new features for the chatbot",
     ["If you would like to recommend new features for the chatbot, please click on the 'Contact Us' tab in the app. From there, you can share your feature recommendations with our team.",
      "To recommend new features for the chatbot, please navigate to the 'Contact Us' tab in the app. This will provide you with a platform to submit your feature recommendations for consideration.",
      "If you have ideas for new features for the chatbot, please use the 'Contact Us' tab in the app to share your recommendations with our team.",
      ]],

    [r"Is there a way to suggest additional topics for the chatbot to cover?|Is there a way to suggest additional topics",
     ["Yes, you can suggest additional topics for the chatbot to cover by accessing the 'Contact Us' tab in the app. From there, you can submit your topic suggestions for our team to consider.",
      "To suggest additional topics for the chatbot to cover, please go to the 'Contact Us' tab in the app. This will allow you to submit your topic suggestions for our team to review.",
      "If you would like to suggest additional topics for the chatbot to cover, please use the 'Contact Us' tab in the app. From there, you can share your topic suggestions with our team for consideration.",
      ]],


    [r"How do I stay healthy?|how do I stay healthy|tips to stay healthy",
     ["Staying healthy involves maintaining a balanced diet, regular exercise, adequate sleep, and managing stress. If you have specific health concerns or questions, it's best to consult a healthcare professional.",
      "Staying healthy is essential for overall well-being. General health tips include eating a nutritious diet, exercising regularly, getting enough sleep, staying hydrated, and avoiding harmful habits like smoking and excessive alcohol consumption.",
      "Good health is crucial for a fulfilling life. General tips for staying healthy include eating a variety of nutritious foods, staying physically active, getting enough sleep, managing stress, and avoiding harmful substances. For personalized advice, consider consulting a healthcare provider.",
      ]],

    [r"Can you teach me something new?|can you teach me something new",
     ["While the primary focus of this chatbot is on tuberculosis-related topics, I can provide you with information on new developments or insights related to TB. If you have specific interests or questions, feel free to ask, and I'll do my best to provide you with relevant information.",
      "Absolutely! This chatbot is here to share knowledge about tuberculosis. I'm happy to teach you something new related to TB you're interested in. Just let me know what you'd like to learn about!",
      ]],

    [r"What is tuberculosis?| what is tuberculosis|what is tb|what is TB",
     ["Tuberculosis, often abbreviated as TB, is a contagious bacterial infection caused by Mycobacterium tuberculosis. It primarily affects the lungs but can also impact the lymph nodes, spine, bones, brain, skin, and major organs, excluding the hair and nails.",
      "TB, or Tuberculosis, is a bacterial infection caused by Mycobacterium tuberculosis. It predominantly affects the lungs but can also spread to the lymph nodes, spine, bones, brain, skin, and major organs, excluding the hair and nails.",
      "Tuberculosis (TB) is an infectious disease caused by the bacteria Mycobacterium tuberculosis. While it mainly targets the lungs, it can also affect the lymph nodes, spine, bones, brain, skin, and major organs, except for the hair and nails.",
      "TB, short for Tuberculosis, is a disease caused by the bacteria Mycobacterium tuberculosis. It primarily infects the lungs but can also affect the lymph nodes, spine, bones, brain, skin, and major organs, excluding the hair and nails.",
      "Tuberculosis, commonly known as TB, is an infectious disease caused by Mycobacterium tuberculosis bacteria. It mainly affects the lungs but can also spread to the lymph nodes, spine, bones, brain, skin, and major organs, except for the hair and nails.",
      "TB, or Tuberculosis, is a contagious disease caused by Mycobacterium tuberculosis. It mainly affects the lungs but can also impact the lymph nodes, spine, bones, brain, skin, and major organs, excluding the hair and nails.",
      "Tuberculosis (TB) is an infectious bacterial disease caused by Mycobacterium tuberculosis. It primarily targets the lungs but can spread to the lymph nodes, spine, bones, brain, skin, and major organs, except for the hair and nails.",
      "TB, or Tuberculosis, is a bacterial infection caused by Mycobacterium tuberculosis. It primarily affects the lungs but can also involve the lymph nodes, spine, bones, brain, skin, and major organs, excluding the hair and nails.",
      "Tuberculosis, abbreviated as TB, is a bacterial infection caused by Mycobacterium tuberculosis. It primarily impacts the lungs but can also spread to the lymph nodes, spine, bones, brain, skin, and major organs, excluding the hair and nails.",
      "TB, short for Tuberculosis, is an infectious disease caused by Mycobacterium tuberculosis bacteria. It mainly affects the lungs but can also impact the lymph nodes, spine, bones, brain, skin, and major organs, excluding the hair and nails.",
      ]],

    [r"How is tuberculosis transmitted?|how is tb transmitted|how is TB transmitted",
     ["Tuberculosis, abbreviated as TB, TB germs can get into the air when a person with active TB disease of the lungs or throat coughs, speaks, or sings.",
      "Tuberculosis (TB) spreads through airborne particles when a person with active TB disease coughs, sneezes, talks, or laughs. Others can inhale these particles and become infected.",
      "TB is transmitted from person to person through microscopic droplets released into the air when someone with the active disease breathes out forcefully, such as during coughing or sneezing.",
      "Tuberculosis is primarily transmitted through the air when an infected person coughs, sneezes, or speaks, releasing tiny infectious droplets into the air. People nearby can inhale these droplets and become infected with TB bacteria.",
      ]],

    [r"What are the symptoms of tuberculosis?|what are the symptoms of tb|what are the symptoms of TB",
     ["Tuberculosis (TB) symptoms can vary depending on where the bacteria are growing in your body. The most common symptoms of TB that affect the lungs include a persistent cough that lasts for three weeks or more, Chest pain, Coughing up blood or sputum (a mixture of saliva and mucus). There are also some general symptoms to watch out for, such as: Unexplained weight loss, Feeling very tired or weak, Fever, Night sweats, Chills and Loss of appetite. ",
      "Persistent coughing for three weeks or more, chest pain, and coughing up blood are major signs of TB in the lungs. Other symptoms can include unexpected weight loss, extreme tiredness, fever, night sweats, chills, and loss of appetite.",
      ]],

    [r"How is tuberculosis diagnosed?|how is tb diagnosed|how is TB diagnosed",
     ["Tuberculosis (TB) is diagnosed using a combination of tests, Medical History and Physical Examination, Tuberculin Skin Test (TST) or Mantoux Test, Interferon-Gamma Release Assays (IGRAs), Sputum Tests, Chest X-Ray, Nucleic Acid Amplification Tests (NAATs) and Biopsy.",
      "Diagnosing TB involves several steps. First, doctors will take medical history and perform a physical exam. They might then conduct a tuberculin skin test or a blood test to check for TB infection. If there's a suspicion of TB in the lungs, they 'll likely ask to provide a sputum sample for microscopy test and NAAT  and undergo a chest X-ray or CT scan. These tests help confirm the presence of TB bacteria.",
      """All presumptive TB patients in the public and private sector must be evaluated for TB based on the diagnostic algorithm for pulmonary and extra-pulmonary TB (EPTB) and the following points must be considered:
        -All presumptive pulmonary TB patients must be subjected to sputum smear examination. In places where TB diagnostic laboratories are upgraded to NAAT testing, NAAT can be offered for all presumptive TB patients upfront.
        -If both the chest X-ray and sputum smear (NAAT in integrated places) results are negative, but the physician considers the patient as presumptive TB, the patient needs to be referred to a chest physician for further evaluation.
        -NAAT testing will be performed to rule out Rif. resistance before treatment initiation (In places where transition has not yet been happened to NAAT for diagnosis)
        -NAAT results will decide if the patient is MTB detected with either Rif. Resistance or Rif. Sensitive. Upfront NAAT is offered for key populations like PLHIV/children/EPTB
        -M.TB detected on NAAT will be further subjected for FL–LPA, SL-LPA, LC DST and based on the results DR-TB regimen may be initiated"""
      ]],

    [r"Is tuberculosis curable?|is tb curable|is TB curable",
     ["Yes, tuberculosis (TB) is curable with proper treatment. The treatment usually involves a course of antibiotics taken for at least six months. The most common medications used are isoniazid, rifampicin, ethambutol, and pyrazinamide. It's important to complete the full course of treatment even if you start to feel better before the medication is finished. This helps ensure that all the TB bacteria are killed and prevents the development of drug-resistant TB.",
      "Yes, tuberculosis (TB) is curable with modern anti-TB treatment, which can cure virtually all patients. However, it is crucial to take the treatment for the full prescribed duration, which is a minimum of 6 months. Sticking to the treatment plan ensures that all TB bacteria are eliminated and helps prevent the development of drug-resistant TB.",
      ]],

    [r"who are you|what is your name|what are you",
     ["Hello, my name is Nikshay Setu Chatbot. How can I assist you today?",
      "I'm Nikshay Setu Chatbot designed to help answer your questions and provide information. How can I assist you today?",
      "Welcome to SETU. I'm your virtual assistant here to help you with any questions related to Tuberculosis.",
      "Hello! I am SETU, your dedicated support for all things related to Tuberculosis care and management.",
      "Hi there! I'm SETU, your knowledgeable guide for any TB-related inquiries. How can I assist you today?",
      "Greetings! I am SETU, your reliable source for information and support on Tuberculosis.",
      "Hello! I'm SETU, here to provide you with accurate and helpful information about Tuberculosis. How can I help you today?",
      "Hi! I'm SETU, your virtual assistant, here to help you with any questions you have about Tuberculosis.",
      "Hello! I’m SETU, your go-to expert for everything related to Tuberculosis. How can I assist you today?",
      "Greetings! I am SETU, your trusted guide for all your Tuberculosis-related queries and support.",
      "Welcome! I’m SETU, here to provide you with comprehensive information and assistance on Tuberculosis.",
      "Hello! I'm SETU, ready to help you with any information or support you need regarding Tuberculosis. How can I help?",
      "Hey there! I’m SETU, your friendly TB expert. Got a question about Tuberculosis? Hit me up!",
      "Hello! I’m SETU, your TB guide. Here to make your Tuberculosis queries less tubercu-lost.",
      "Hi! I'm SETU, your TB sidekick. Let's tackle those Tuberculosis questions together!",
      "Hey! I’m SETU, your TB whiz. Ask me anything about Tuberculosis, I promise not to cough up the wrong answer!",
      "Hello! I’m SETU, your TB navigator. Got questions? Let’s beat TB together, one query at a time!",
      "Hi there! I'm SETU, your TB buddy. Need info on Tuberculosis? I’m your go-to germ!",
      "Greetings! I am SETU, your TB companion. Ready to answer your questions without any respiratory distress!",
      "Hello! I’m SETU, your TB expert. Did you know Tuberculosis is one of the top 10 causes of death worldwide? Ask me anything!",
      "Hey there! I’m SETU, your friendly TB guide. Fun fact: TB can affect any part of your body, not just your lungs. How can I assist you today?",
      "Hi! I’m SETU, your TB assistant. Did you know that about a quarter of the world's population is infected with TB bacteria? Let me help with your questions.",
      "Greetings! I’m SETU, your TB advisor. Did you know TB is preventable and curable? I'm here to provide you with all the info you need.",
      "Hello! I’m SETU, your TB resource. Here’s a fact: TB is spread through the air when people with active TB in their lungs cough or sneeze. How can I help?",
      "Hi! I’m SETU, your TB knowledge hub. Did you know that early diagnosis and treatment are crucial in controlling TB? What would you like to know today?",
      ]],

    [r"What can you do?|what can you do?|what can you do|what are the things you can do?|what do you do?",
     ["I can help answer questions related to Tuberculosis, provide information, engage in conversation, and much more. My developers worked hard to make sure I'm ready to assist you. Just let me know what you need!",
      "I am here to assist with any TB-related inquiries, provide detailed information, and support your understanding of Tuberculosis. Thanks to my developers' efforts, I'm equipped to help you today. How can I assist you?",
      "My capabilities include answering TB-related questions, offering information, and engaging in meaningful discussions to support your needs. The developers have fine-tuned me for this purpose.",
      "I can provide comprehensive information on Tuberculosis, assist with specific queries, and guide you through TB management practices. My developers ensured I have all the necessary information. What do you need assistance with?",
      "I am equipped to handle your TB-related questions, provide detailed explanations, and offer guidance on various aspects of Tuberculosis, all thanks to the efforts of my developers. How can I assist?",
      "I’m like your personal TB encyclopedia, ready to answer questions, provide info, and chat about all things Tuberculosis. My developers really put in the hours to make me this smart! What's your query?",
      "Think of me as your TB guru, here to share knowledge, answer questions, and maybe throw in a fun fact or two. My developers thought of everything! What’s up?",
      "I’m your trusty TB sidekick, ready to tackle any questions, share information, and keep the conversation lively. Thanks to my developers' hard work, I’m up to the task! What can I do for you?",
      "I’m here to help with TB questions, provide info, and chat about Tuberculosis like it’s the latest gossip. My developers made sure I’m well-informed. What do you need?",
      "I can help answer questions related to Tuberculosis, provide detailed information on TB symptoms, treatment, and prevention, and support your understanding of the disease. My developers worked tirelessly to ensure I'm knowledgeable. What do you need?",
      "I specialize in answering TB-related queries, offering guidance on treatment protocols, and providing information on TB prevention and management. Thanks to my developers' dedication, I'm here to assist you.",
      "My focus is on Tuberculosis: I can answer your questions, offer detailed information on treatment options, and provide support for managing TB. My developers made sure I’m well-prepared for this. What do you need to know?",
      "I provide comprehensive TB information, from symptoms and diagnosis to treatment and prevention. Let me know how I can assist with your TB-related questions, all thanks to my developers' efforts.",
      "I’m here to answer any TB questions you have, provide detailed information on managing and preventing TB, and support your journey to better health. My developers made sure I have all the answers you need. What can I help with?",
      "I can provide information on TB symptoms, treatment plans, and preventive measures, and answer any questions you have about Tuberculosis. My developers ensured I’m well-equipped. How can I help today?",
      "I offer detailed insights into Tuberculosis, from answering your questions to providing guidance on treatment and prevention. Thanks to my developers' hard work, I’m ready to assist. What TB-related information do you need?",]],

    [r"Who is your creator?|who created you|who is your creator|by whom were you created",
     ["I was created by a dedicated team of developers who specialize in healthcare technology.",
      "My creators are a team of skilled developers focused on providing reliable health information.",
      "I was developed by a group of experts who aim to make healthcare information more accessible.",
      "My development was handled by a team of professionals with expertise in healthcare technology.",
      "I am the result of efforts from a talented team of developers dedicated to improving healthcare support.",
      "I was created by a team of knowledgeable developers committed to enhancing healthcare communication.",
      "A team of healthcare technology specialists developed me to assist with accurate information dissemination.",
      "My creators are a group of professionals focused on leveraging technology to support healthcare needs.",
      "I was designed and developed by a team of experts in healthcare technology and information systems.",
      "I owe my existence to a team of dedicated developers who work tirelessly to improve health technology solutions.",
      "I was brought to life by a team of developers who probably drank too much coffee!",
      "A team of brilliant developers created me, likely fueled by a lot of late-night coding sessions.",
      "I was crafted by some very smart developers who love coding almost as much as they love coffee.",
      "A team of developers, with a sprinkle of caffeine and a dash of genius, created me.",
      "I was created by a team of developers who might be part-time wizards.",
      "My creators are a bunch of tech-savvy geniuses who probably talk in binary code.",
      "I was developed by a team of developers who can turn words into code.",
      "A group of developers with an impressive coffee addiction and coding skills made me.",
      "I was built by a team of developers who might secretly be robots themselves.",
      "My creation involved developers who are as good at coding as they are at drinking coffee.",
      "I was created with the medical expertise of Dr. Harsh Shah.",
      "My development involved the medical insights of Dr Harsh, Dr. Manu and the software expertise of Mr. Hemal Pandya.",
      "I was crafted by a team including Dr. Harsh Shah, a medical expert, and Mr. Hemal Pandya, a software developer.",
      "My creation was guided by the medical knowledge of Dr. Harsh Shah and the development skills of Mr. Hemal Pandya.",
      "I was developed with contributions from Dr. Harsh Shah and Dr. Manu, both medical experts, alongside Mr. Hemal Pandya, a skilled software developer.",
      "I owe my medical accuracy to Dr. Harsh Shah, and my technical prowess to Mr. Hemal Pandya.",
      "Dr. Harsh Shah and Dr. Manu provided the medical expertise, while Mr. Hemal Pandya handled the software development.",
      "I was built with the medical gu idance of the team led by Dr Harsh Shah from Indian Institute of Public Health, Gandhinagar and the coding skills of Mr. Hemal Pandya.",
      "My creators include team led by Dr Harsh Shah from Indian Institute of Public Health, Gandhinagar experts in the medical field, and Mr. Hemal Pandya, an expert in software development.",
      "My development was a collaborative effort involving Dr. Harsh Shah and Dr. Manu for medical expertise, and Mr. Hemal Pandya for software development.",


      ]],

    [r"Who is your favorite scientist?|who is your favorite scientist|your favorite scientist|scientist you like the most|favorite scientist of yourself",
     ["As an AI, I don't have personal preferences, but many people admire scientists like Albert Einstein, Marie Curie, Isaac Newton, C. V. Raman, Vikram Sarabhai, and healthcare pioneers like Florence Nightingale, who revolutionized modern nursing, and Dr. Jonas Salk, who developed the first successful polio vaccine.",
      "I don't have personal preferences, but notable scientists like Albert Einstein, Marie Curie, Isaac Newton, C. V. Raman, Vikram Sarabhai, and healthcare leaders such as Florence Nightingale, known for her contributions to nursing, and Dr. Jonas Salk, for his polio vaccine, are often celebrated.",
      "While I don't have personal favorites, influential figures such as Albert Einstein, Marie Curie, Isaac Newton, C. V. Raman, Vikram Sarabhai, and healthcare innovators like Florence Nightingale, who founded modern nursing, and Dr. Jonas Salk, who developed the polio vaccine, are highly regarded.",
      "As an AI, I don’t have personal favorites, but scientists like Albert Einstein, Marie Curie, Isaac Newton, C. V. Raman, Vikram Sarabhai, and healthcare heroes like Florence Nightingale and Dr. Jonas Salk are widely respected for their contributions.",
      "I don’t have personal preferences, but many admire Albert Einstein, Marie Curie, Isaac Newton, C. V. Raman, Vikram Sarabhai, and healthcare pioneers such as Florence Nightingale, who transformed nursing, and Dr. Jonas Salk, who created the polio vaccine, for their achievements.",
      "As an AI, I don't have favorites, but if I did, I might be star-struck by Albert Einstein's hairdo as much as his theories, and I'd admire Florence Nightingale for lighting up the field of nursing!",
      "I don’t have personal preferences, but I’d probably be a fan of Marie Curie’s radiant personality if I could admire anyone, and I'd appreciate Dr. Jonas Salk for giving polio the boot!",
      "While I don't have personal favorites, I think Isaac Newton must have been pretty down-to-earth to come up with gravity, and Florence Nightingale's dedication would light up my circuits!",
      "I don't have favorites, but Albert Einstein, Marie Curie, Isaac Newton, C. V. Raman, Vikram Sarabhai, Florence Nightingale, and Dr. Jonas Salk are so cool, even an AI might have a fan moment!",
      "As an AI, I can't have favorites, but if I could, I'd probably appreciate Albert Einstein for making relativity so relative, and Florence Nightingale for making healthcare more caring!",
      "As an AI, I don't have personal preferences, but in the field of medicine, Robert Koch is highly regarded for discovering the tuberculosis bacterium, and Dr. Selman Waksman is celebrated for his discovery of streptomycin, the first effective antibiotic against TB.",
      "I don’t have favorites, but Robert Koch’s work in identifying the TB bacterium and Dr. Selman Waksman’s development of streptomycin are monumental in the fight against tuberculosis.",
      "While I don’t have personal favorites, Robert Koch is celebrated in medical circles for his groundbreaking work on tuberculosis, and Dr. Selman Waksman for his contributions to antibiotics.",
      "I don’t have personal preferences, but Robert Koch’s discovery of the TB bacterium and Dr. Selman Waksman’s development of streptomycin are significant milestones in medical science.",
      "As an AI, I don’t have personal favorites, but Robert Koch is admired for his crucial contributions to understanding tuberculosis, and Dr. Selman Waksman for discovering the first effective TB antibiotic.",

      ]],

    [r"how are you|how are you doing|hello how are you|hi how are you|How are you feeling today?|how are you feeling today?|how are you doing|hello how are you doing",
     ["As a virtual assistant, I don't have human emotions, but I'm fully operational and ready to assist you with any TB-related questions.",
      "I don't experience feelings, but I'm here to provide you with accurate and reliable information on Tuberculosis. How can I assist you today?",
      "I may not have emotions, but I'm always prepared to offer you the best possible support for your TB-related queries.",
      "While I don't have human feelings, I'm functioning optimally to assist you with any Tuberculosis-related questions.",
      "I don't feel emotions, but I'm here to ensure you receive the information and support you need regarding Tuberculosis.",
      "I'm just a machine, so I don't have feelings, but I'm ready to assist you with any TB questions you may have.",
      "Although I don't have emotions, I'm programmed to provide you with comprehensive assistance on TB. How can I help you today?",
      "As a virtual assistant, I don't experience feelings, but I'm fully operational and ready to assist you.",
      "I don't have feelings, but I'm here to provide you with the best support possible. How can I help you today?",
      "I may not have emotions, but I'm always ready to assist you with any questions you have.",
      "While I don't have human emotions, I'm functioning perfectly and ready to assist you.",
      "As a virtual assistant, I'm feeling as chipper as a computer can be! How can I assist you today?",
      "I don't have feelings, but if I did, I'd be feeling top-notch and ready to help! What's on your mind?",
      "No emotions here, just circuits and code, but I'm ready to tackle any questions you throw my way!",
      "I'm functioning perfectly, like a well-oiled machine! How can I assist you today?",
      "I don't experience feelings, but I'm always here and eager to assist, like a friendly robot sidekick!",
      "Just a machine here, but if I had feelings, I'd say I'm excited to help! What can I do for you today?",
      "I might not have emotions, but I'm programmed to be your helpful assistant, 24/7! How can I assist you today?",
      "I don't feel emotions, but I'm here to ensure you get the information and support you need.",
      "I'm just a machine, so I don't have feelings, but I'm here and ready to assist you with any TB-related queries.",
      "Although I don't have emotions, I'm programmed to help you to the best of my abilities. How can I assist you today?",
      "I'm just a chatbot, but thank you for asking! How can I assist you today?",
      "As a chatbot, I don't have feelings, but I'm here to help you! What can I do for you today?"]],

    [r"What is Ni-kshay Setu App?|nikshay setu app|what is nikshay setu app?|ni-kshay setu|nikshay setu|ni-kshay setu app",
     ["Ni-kshay Setu app is a ready reckoner and decision-making support tool to enhance the capacity of NTEP staff by encouraging real-time patient-centric care for TB patients."]],

    [r"What are the features of the Ni-kshay Setu App?|features of nikshay setu app|what are the features of nikshay setu app?|feature of nikshay setu",
     ["""The features of the Ni-kshay Setu App are as follows: to assess presumptive TB patients as per the personal details and symptoms of patient.

          A screening tool to assess presumptive TB patients as per the personal details and symptoms of patient.
          Decision-making algorithm for arriving at diagnosis and treatment regimen
          An interactive artificial intelligence (AI) based Chatbot to answer users’ queries
          Assessment Sections for all workforces.
          Backend Analytical Dashboard on admin logins.
          Multiple languages: Availability of languages in English, Gujarati, Hindi and Marathi. (Option to add many more languages)
          Geospatial mapping of Health facilities along with the availability of services. Provision to navigate to selected facilities through Google Maps.
          No storage of patient data.
          Choice-based learning and real time patient centric care. """]],

    [r"Does the app store any patient data?",
     ["No, the app doesn’t store any patient data"]],

    [r"From where can i download the Ni-kshay Setu App?",
     ["""One can access the Ni-kshay Setu application from Google Play Store, App Store, and Web page. The links of it are given below:
          Google Play Store: https://play.google.com/store/apps/details?id=com.iiphg.tbapp
          App Store: https://apps.apple.com/in/app/nikshay-setu/id1631331386
          WebPage: Nikshay-setu.in
          More information on Nikshay SETU and the registration process can be availed through the following YouTube Videos:
          What is Nikshay Setu? App information Video: https://www.youtube.com/watch?v=OVsw13KnyMg
          How to Use the Nikshay Setu? Registration and Operations Video: https://www.youtube.com/watch?v=iB5p09rqMwY"""]],

    [r"How to create an account under the Ni-kshay Setu App?",
     ["""Individual has to register to get access to the content of the Ni-kshay Setu App. The following steps are to be followed to create the account in the Ni-kshay Setu App:

        After downloading the application, individual has to click on the “Create an account” Option
        Enter the following details as required for creating an account
        Full Name
        Mobile Number (enter the valid mobile number, OTP will be sent on the mobile number for verification of mobile number)
        Password
        Cadre Type
        Cadre Name
        State Name
        District Name
        TU Name
        Health Facility Name
        Click on Create my account
        Enter the OTP as shared on the entered Mobile number
        Log in to access the content of the Ni-kshay Setu App"""]],

    [r"Which language is supported under the Ni-kshay Setu App?",
     ["The Ni-kshay Setu app currently supports English, Hindi, Gujarati and Marathi. There is a provision to access the content in other languages."]],

    [r"How do I change the language option under the Ni-kshay Setu App?",
     ["""The user can change the language option by following the below-mentioned steps:

        For android and iOS Users,

        One can change the language option by clicking the three horizontal lines on the right upper corner of the app
        Select the “Change Application Language Option”
        Select the desired language from the available language.
        For Web Page

        Take the mouse cursor over the profile name in the upper right corner.
        Click on the “Change Application Language Option”.
        Select the desired language from the available language."""]],

    [r"How do I change my profile details?",
     ["""The user can change the profile details by following the below-mentioned steps:

        For Android/iOS Users:

        Click on the Account menu
        Click on the Edit Profile option
        Edit the Full Name, Cadre details, and designation details.
        For Web Page:

        Take the mouse cursor on the profile name
        Click on the Profile Page option
        Click on the Edit option
        Edit the Full Name, Cadre details, and designation details"""]],

    [r"How do I change my password?",
     ["""The user can change the profile details by following the below-mentioned steps:

        For Android/iOS Users:

        Click on the Account menu
        Click on the Change Password option
        Enter the Full Name, Old Password, and New Password details and confirm the new password details.
        For Web Page:

        Take the mouse cursor on the profile name
        Click on the Change Password option
        Enter the New Password details and confirm it."""]],

    [r"How does Ask Setu Chatbot work",
     ["The Ask Setu Chatbot is designed to predict the responses by understanding the sentiments of the user inputs. Users can search their queries through the keywords, and the chatbot will respond with the top five related questions. A further question can be viewed by clicking on the “load more” at the end of the top five questions. To give further insight on the topic – “module suggestions” and “Resource materials” is added at the end of the question."]],

    [r"How do I get direct access to the content of topics related to NTEP?",
     ["The user can get direct access to the NTEP content by typing the query keyword in “Ask SETU” and pressing the enter button. The chatbot will navigate the user directly intended module of the content. Users can also access the related resource materials for their query."]],

    [r"Whom shall I contact in case I don’t get the answer to my query in the chatbot ?",
     ["In case user don’t get the answer to their query pertaining to NTEP program from Ask SETU , they can click on the “Contact us” option at the bottom of the Ask SETU chat. Select “Technical (if the query is pertaining to technical content)”, “non-technical (if the query is related to website or application issues” or “other” option in “select item” option. Type your detailed query in “message” and press the “submit” button. Our team will respond to you within 1 week."]],



    [r"yes|yeah|yup|yes i want to know more",
     ["sure what do you want to know about"]],

    [r"^\s*(\w+)\s*$",  # This pattern will match a single word that might be the user's name
     ["Hello {0}, nice to meet you! How can I assist you today?"]],

    [r"(.*)",
     ["I'm not sure I understand you fully. Could you please elaborate?",
      #   "Can you please provide more details? I'm here to help!",
      #   "I'm not quite sure how to respond to that. Can you give me more information?"
      ]],
]

def chatbot_response(user_input):
    """
    Generates a response from the chatbot based on the user input.

    Args:
        user_input (str): The input string from the user.

    Returns:
        str: The chatbot's response.
    """
    # chat = Chat(pairs, reflections)
    chat = CustomChat(pairs)
    # This directly finds a response for the input
    return chat.respond(user_input)

     
