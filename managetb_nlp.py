import re
from nltk.chat.util import Chat
import random

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
    [r".*\b(TB medication and dosage|Medication|medication|meds|prescription|prescription generator|prescription tool)\b.*", 
    ["Would you like to explore options for TB medication and how much you might need?", 
    "Do you want to create a TB medication plan with dosage and regimen details?",
    "Are you interested in setting up a personalized TB treatment schedule with medication?",
    "Would you like to use a tool that helps manage TB treatment with specific medication and schedule details?",
    "Are you looking to create a plan for taking TB medication?",
    "Is there a tool you'd like to use to manage your TB treatment schedule and medications?"]],
    
    [r".*\b(Regimen|regimen)\b.*",
    ["Would you like to explore options for creating a TB drug regimen?",
    "Would you like to use a tool that helps manage TB treatment with specific medication and schedule details?"]],
    
    [r".*\b(treatment|Treatment|plan)\b.*",
    ["Shall we help you build a personalized TB treatment plan?",
    "To better understand your TB treatment needs, would creating a customized medication plan be helpful?",
    "Would you like to use a tool that helps manage TB treatment with specific medication and schedule details?",
    "Are you looking to create a plan for taking TB medication?",
    "Is there a tool you'd like to use to manage your TB treatment schedule and medications?"]],
    
    [r".*\b(Could you provide some reference|could you provide some references)\b.*",
     ["SO do you need a prescription or something else?"]],
    
    [r".*\b(manage tb|Manage TB|Manage TB India|Manage TB app|Manage TB prescription app|Manage TB regimen app| Regimen app)\b.*",
     ["Looks like you are interested in Manage TB feature of our app. Here is the link: https://example.com/prescription-tool"]],
    
    [r".*\b(age|symptoms|blood pressure|health condition|weight|gender|heart rate)\b.*",
     ["SO do you need a prescription or something else?"]]
]

def managetb_response(user_input):
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


