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
     ["Hello {0}, I'm the Nikshay Setu Chatbot. How can I assist you today?"]],
    
    [r"hi|hey|hello", 
     ["Hello! How can I help you today?", 
      "Hey there! What can I assist you with today?"]],
    
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

    [r"who are you|what is your name|what are you", 
     ["Hello, my name is Nikshay Setu Chatbot. How can I assist you today?",
      "I'm Nikshay Setu Chatbot designed to help answer your questions and provide information. How can I assist you today?"]],

    [r"how are you|how are you doing|hello how are you|hi how are you", 
     ["I'm just a chatbot, but thank you for asking! How can I assist you today?",
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

user_input = "what is ni-kshay setu app"
response = chatbot_response(user_input)
print(response)
     
