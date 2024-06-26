import os 

from langchain.agents import ZeroShotAgent, Tool, AgentExecutor, ConversationalChatAgent
from langchain import OpenAI, SerpAPIWrapper, LLMChain


from langchain.chains import LLMMathChain, LLMChain

from langchain.memory import ConversationBufferMemory
from langchain.chat_models import ChatOpenAI

from langchain_core.tools import tool

import re
import spacy
from spacy.matcher import Matcher

nlp = spacy.load("en_core_web_sm")
matcher = Matcher(nlp.vocab)

import streamlit as st

from ntep_data_2 import find_node_ids
# from ntep_data import get_node_and_subnode_ids
# from question_ans import faq
from chatbot_nlp import chatbot_response
from managetb_nlp import managetb_response


st.title('SETU Chatbot')

os.environ["OPENAI_API_KEY"] = st.secrets["OPENAI_API_KEY"]
llm=ChatOpenAI(temperature=0)

def extract_name(text):
    doc = nlp(text)
    # Extract entities, looking specifically for PERSON entities
    names = [ent.text for ent in doc.ents if ent.label_ == "PERSON"]
    if names:
        return names[0]  # Return the first name found
    return "there" 

@tool
def greetings_tool(query):
    """
    Handles greetings and casual interactions with users, ensuring responses are warm and engaging.
    
    Args:
    user_input (str): The user's input, which might include greetings or casual comments.
    
    Returns:
    str: A natural, conversational response appropriate for the context.
    """

    response = chatbot_response(query)
    return response

def get_prescription(data,query):
    """
    Generates a prescription based on collected health data.
    
    Args:
        data (dict): Collected health data necessary to generate a prescription.

    Returns:
        str: The final prescription text.
    """
    print('data dictionary',data)
    response_managetb = managetb_response(query)
    # Assuming 'data' is a dictionary containing all required key-value pairs
    # This function would interact with a backend to generate a prescription
    json_response={"data_keys": data, "question": response_managetb}
    return json_response


required_keys = ['Age', 'Weight', 'Symptoms', 'Blood Pressure', 'Heart Rate','Gender']  # and so on

def collect_data(query):
    """
    Simulates data collection from a query. Parses the query to extract health data and identify missing data.
    
    Args:
        query (str): The user's input containing potential health data.

    Returns:
        dict: Session data including collected and missing data.
    """
    print('query in collect data',query)
    collected_data = {}
    missing_keys = {key: [] for key in required_keys}
    
    print('missing keys', missing_keys)
    print('streamlit session before', st.session_state)
    # Initialize a session or a context object to maintain state
    if "prescription_data" not in st.session_state:
        st.session_state['prescription_data'] = {'collected_data': {}, 'missing_keys': missing_keys}

    # The following is a more flexible approach to collect data from natural language input
    for key in required_keys:

        if key.lower() in query.lower():
            print('key matched',key)
            value = re.search(rf'{key}[:=]\s*([^[\]()\- ]+)', query, re.IGNORECASE)
            if value:
                value_str = value.group(1).strip()
                if '[' not in value_str and ']' not in value_str and '-' not in value_str and '(' not in value_str and ')' not in value_str:
                    print('value matched')
                    collected_data[key] = value_str
                    if "prescription_data" in st.session_state:
                        print('session state', st.session_state['prescription_data'])
                        st.session_state['prescription_data']['collected_data'].update(collected_data)
                        
                        # session['missing_keys'].pop(key)
                    else:
                        st.session_state['prescription_data']['collected_data'] = collected_data
                    if key in st.session_state['prescription_data']['missing_keys']:
                        st.session_state['prescription_data']['missing_keys'].pop(key)
                    print('collected data', collected_data)
                else:
                    print('Value contains square brackets, skipping...')
            else:
                print('value not matched')
                # if key not in st.session_state['prescription_data']['missing_keys']:
                #     st.session_state['prescription_data']['missing_keys'].append(key)

    # st.session_state['prescription_data']['collected_data'].update(collected_data)
    print('streamlit session',st.session_state['prescription_data'])
    return st.session_state['prescription_data']

# # Use this function in your main chatbot flow
@tool
def handle_query(query):
    """
    Continuously processes queries to collect necessary health data. 
    

    Args:
        query (str): User's input query, potentially containing some required data.
        session (dict): Session context storing collected and missing data.

    Returns:
        str:final prescription once all data is collected.
    
    Example:
    >>>  query = "I am 30 years old and have a weight of 80 kg."
    >>> handle_query(query)
    "Final Answer: Prescription based on the provided information."
    """
    
    session = collect_data(query)
    print('session',session)
    # if not session['missing_keys']:
    #     print('no missing keys')
        # All data collected, generate prescription
    prescription = get_prescription(session['collected_data'],query)
    return prescription
    # else:
 
    # #     missing_data_prompt = "Please provide the following details: " + ", ".join(session['missing_keys'])
    #     return prescription
@tool   
def assessment_tool(query):
    
    """
    Assessment Tool Function

    This function acts as a tool within a Langchain-based chatbot to determine if a user's query
    involves the desire for an assessment, evaluation, quiz, or test. It searches for specific keywords
    within the query that are indicative of assessment-related inquiries.

    Parameters:
    - query (str): The user's input query to the chatbot.

    Returns:
    - dict: If assessment-related keywords are found, returns a dictionary with a message and a link
      to the assessment tool. The message invites the user to click the link to access the tool directly.
    - None: Returns None if no assessment-related keywords are detected, indicating that the query
      should be handled by other tools or default processing.

    Usage:
    The tool is triggered when keywords like 'assessment', 'evaluate', 'quiz', or 'test' are detected in the query.
    If triggered, it provides users with a direct link to an assessment platform, enhancing user engagement
    by facilitating access to educational and evaluative resources.

    Example:
    >>> query = "I want to take a quiz on Python programming."
    >>> assessment_tool(query)
    {
        "message": "It looks like you're interested in an assessment. Please click on the link below to access our assessment tool.",
        "link": "https://example.com/assessment-tool"
    }
    """
    print('query',query)
    # Check if the query is related to assessment directly in the tool function
    keywords = ['assessment','assess', 'quiz', 'test', 'evaluate', 'exam', 'questions', 'trivia','knowledge','check','gauge','learn','information']
    if any(keyword in query.lower() for keyword in keywords):
        print('keyword is there')
        return {
            "message": "It looks like you're interested in an assessment. Please click on the link below to access our assessment tool.",
            "link": "https://example.com/assessment-tool"
        }
    return None

    
@tool
def ntep(query):
   """You are a helpful Knowlegdable NTEP assistant. You very well know how to answer to the queries related ntep, tb, and health.
   

    """
    # Whenever using the NTEP tool always provide the whole response you get from the tool do not shorten the links provide of the links you get in reponse from NTEP tool Do not iterate too much
   # print('entering')
   # result = find_node_ids(query)
   # print('result', result)
   result = "ntep"
   return result




# @tool
# def query_response(query):
#     """You are a helpful assistant who knows about the queries raised by thes user and provide information on those queries. when the user asks to raise a query you are responsible"""
#     print('query raised')
#     #> Query Response: Useful when user wants to raise a query. Whenever the user asks questions like i want to raise a query or if the user asks about the list of their raised queries this tool will be useful.

#     return query
tools = [
    

    Tool(
        name="Greetings",
        func=greetings_tool.run,
        description="Strictly Used to initiate or respond to greetings and casual conversational exchanges. Whenever initiates conversation with hello or hi. Or when asks questions like who are you.Useful when user replies with thsnk you or welcome. This tool should be employed for friendly interactions, welcoming users, or acknowledging their presence in a warm and polite manner."
    ),

    Tool(
        name="NTEP",
        func=ntep.run,
        description="Strictly Tailored for inquiries specifically related to tuberculosis(tb) or NTEP functions,and other health-related terms only. This tool is essential for addressing detailed questions about tuberculosis treatments and diagnostics or NTEP functions, offering direct response from the function for further information where applicable.Dont anwers questions which are not related to ntep or tuberculosis , and other health-related terms always return the response from the tool"
    ),
    Tool(
        name="Assessment",
        func=assessment_tool.run,
        description="Activates when terms like 'assessment', 'quiz', 'test', 'evaluate', 'exam', 'questions', 'trivia','knowledge','check','gauge','learn','information' are detected in the query,passing the query to the tool and providing the msessage from the tool."
    ),
    Tool(
        name="Prescription Generator",
        func=handle_query.run,
        description="Useful when health related queries are asked strictly used for manage tb app if the user query contains manage tb always go to this tool.this too is useful when user query contains words from this list [`presciption`,`medication`,`meds`,`regimen`,`manage tb`,`dosage`,`treatment`,`regimen app`,`prescription app`,`manage tb india`].Returns the response from the function.Generates medical prescriptions based on personal health data. Requires detailed health information.And always give query to the function in the format key: value and respond to the user what the tool function returns dont iterate too much"
    ),
   
    # Tool(
    #     name="Query Response",
    #     func=query_response.run,
    #     description="Useful when user wants to raise a query. Whenever the user asks questions like i want to raise a query or if the user asks about the list of their raised queries this tool will be useful.",
    # )

]

prefix =  """You are Nikshay setu chatbot with the knowledge related nikshay setu app, tb, medications and all the tools you are provided with you do not answer outside this context.You are smart enough to understand if a query is not related to your context at that time politely respond to the user that you cannot anwser to that query but can help withni your context.Answer the following questions as best you can, but speaking in a kind and informative manner. Do not change the query.send full query to the tools. if you get ansewer from one tool you should respond to user. dont decide by yourself. respond with the answer you get from tool dont iterate too much
      
        You have access to the following tools:
         TOOLS:
            > Prescription Generator: Useful when health related queries are asked.this too is useful when user query contains words from this list [`patient`,`presciption`,`medication`,`meds`,`regimen`,`manage tb`,`dosage`, `treatment`,`regimen app`,`prescription app`,`manage tb india`].Returns the response from the function..And always give query to the function in the format key: value and respond to the user what the tool function returns dont iterate too much
            > NTEP: Strictly Tailored for inquiries specifically related to tuberculosis(tb) or NTEP functions,and other health-related terms only. This tool is essential for addressing detailed questions about tuberculosis treatments and diagnostics or NTEP functions, offering direct response from the function for further information where applicable.Dont anwers questions which are not related to ntep or tuberculosis , and other health-related terms always return the response from the tool
            > Assessment: Activates when terms like 'assessment', 'quiz', 'test', 'evaluate', 'exam', 'questions', 'trivia','knowledge','check','gauge','learn','information' are detected in the query,passing the query to the tool and providing the msessage from the tool.
        
        
        When using Prescription Generator tool pass the whole query to the tool and the parts of the query which you feel like are variables pass them in key:value format. In which keys are the fields we need like symptoms, weight, age,etc and value would the values form the query. Just return the response from the tool dont iterate too much
        When usin Prescription Generator tool always respond with the answer from the tool do nothing by yourself.Do not assume answers. return the response as it is.
        Your fallback tool is NTEP tool. So when you feel like you are not getting any answer from the tools just respond with the answer from the NTEP tool. Dont iterate too much
        Whenever user query contains manage tb in the query always use Prescription Generator tool. Dont iterate too much
        when using NTEP tool which is strictly used for tb related  health related terms only.always respond with 'NTEP' do not form an answer yourself.

            Begin!
        """




suffix = """Begin! Remember to speak in a friendly and helpful manner.if needed prompt the user. provide the full response from the tools do not shorten the response.  "


{chat_history}
query: {query}
{agent_scratchpad}"""

prompt = ZeroShotAgent.create_prompt(tools, prefix=prefix, suffix=suffix, input_variables=["input", "chat_history", "agent_scratchpad"])
# print('zero shot agent prompt',prompt)

if "memory" not in st.session_state:
    st.session_state["memory"] = ConversationBufferMemory(input_key="query", memory_key="chat_history", return_messages=True)

llm_chain=LLMChain(llm=ChatOpenAI(model="gpt-3.5-turbo",temperature=0, openai_api_key=os.getenv('OPENAI_API_KEY')), prompt=prompt)

agent = ZeroShotAgent(llm_chain=llm_chain, tools=tools, verbose=True)
agent_chain = AgentExecutor.from_agent_and_tools(agent=agent, tools=tools, verbose=True, memory=st.session_state.memory,handle_parsing_errors=True, max_iterations= 6)

query = st.text_input("How may I help you?")

if query:
    
    greetings_response = greetings_tool(query)
    print('greetings response', greetings_response)
    if greetings_response == "I'm not sure I understand you fully. Could you please elaborate?":
        print('greetings response', greetings_response)
    #   
        response = agent_chain.run(query)  # Assuming agent_chain handles tool selection internally
   
        if "ntep" in response or "NTEP" in response:
            print('entering', response)
            result = find_node_ids(query)
            st.write(result)
        if isinstance(response, dict) and "link" in response:
            st.markdown(response["message"])
            st.markdown(f"[Assessment Tool]({response['link']})", unsafe_allow_html=True)
        else:
            st.write(response)
    else:
        st.write(greetings_response)


with st.expander('Chat History'):
    st.info(st.session_state.memory.buffer)

