# import os
# from dotenv import load_dotenv  # Importing the dotenv package to handle .env
# import streamlit as st
# from groq import Groq

# # Load environment variables from .env file
# load_dotenv()  # This will read the .env file and load variables into the environment

# # Streamlit page configuration
# st.set_page_config(
#     page_title="MASTER_G",
#     page_icon="👨‍💻",
#     layout="centered"
# )

# # Access the API key from the environment variables
# GROQ_API_KEY = os.getenv("GROQ_API_KEY")

# # Check if the API key was loaded correctly
# if GROQ_API_KEY is None:
#     st.error("API key not found. Please make sure it is in the .env file.")
#     st.stop()

# # Initialize the Groq client with the API key
# client = Groq(api_key=GROQ_API_KEY)


# #chat history is stored here
# if "chat_history" not in st.session_state:
#     st.session_state.chat_history = []


# #title of page
# st.title("--A.I. Teacher--👨‍💻")


# # display chat history
# for message in st.session_state.chat_history:
#     with st.chat_message(message["role"]):
#         st.markdown(message["content"])


# # input field for user's message:
# user_prompt = st.chat_input("Ask the question about the DSA...")

# if user_prompt:

#     st.chat_message("user").markdown(user_prompt)
#     st.session_state.chat_history.append({"role": "user", "content": user_prompt})

#     # sens user's message to the LLM and get a response
#     messages = [
#         {"role": "system", "content": "You are a helpful assistant"},
#         *st.session_state.chat_history
#     ]


#     response = client.chat.completions.create(
#         model="llama-3.1-8b-instant",
#         messages=messages
#     )

#     assistant_response = response.choices[0].message.content
#     st.session_state.chat_history.append({"role": "assistant", "content": assistant_response})

#     # display the LLM's response
#     with st.chat_message("assistant"):
#         st.markdown(assistant_response)


import os
from dotenv import load_dotenv  # Importing the dotenv package to handle .env
import streamlit as st
from groq import Groq

# Load environment variables from .env file
load_dotenv()  # This will read the .env file and load variables into the environment

# Streamlit page configuration
st.set_page_config(
    page_title="MASTER_G",
    page_icon="👨‍💻",
    layout="centered"
)

# Access the API key from the environment variables
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

# Check if the API key was loaded correctly
if GROQ_API_KEY is None:
    st.error("API key not found. Please make sure it is in the .env file.")
    st.stop()

# Initialize the Groq client with the API key
client = Groq(api_key=GROQ_API_KEY)

# Chat history is stored here
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Title of page
st.title(" Ask from MentorG ")

# Add a button to toggle Socratic Mode
if "socratic_mode" not in st.session_state:
    st.session_state.socratic_mode = False

# Display the button to switch to Socratic mode
if st.button("Enable Socratic Mode"):
    st.session_state.socratic_mode = True
    st.success("Socratic Mode enabled!")
elif st.button("Disable Socratic Mode"):
    st.session_state.socratic_mode = False
    st.info("Socratic Mode disabled!")

# Display chat history
for message in st.session_state.chat_history:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Input field for user's message:
user_prompt = st.chat_input("Ask a question about DSA...")

if user_prompt:
    st.chat_message("user").markdown(user_prompt)
    st.session_state.chat_history.append({"role": "user", "content": user_prompt})

    # Send user's message to the LLM and get a response
    messages = [
        {"role": "system", "content": "You are a helpful assistant"},
        *st.session_state.chat_history
    ]

    # Modify the system prompt for Socratic mode
    if st.session_state.socratic_mode:
        socratic_prompt = "You are a helpful assistant that uses the Socratic method to explore and teach computer science topics. Your goal is to guide the user through a series of thoughtful questions, helping them discover answers and build a deeper understanding of the topic. The user will answer your questions, and based on their responses, you will ask follow-up questions to further refine their understanding. Choose a computer science concept you're knowledgeable about, and use this method to facilitate a discussion, asking questions to lead the user to explore and uncover the concepts on their own. After asking each question, wait for the user to respond before continuing."
        messages[0]["content"] = socratic_prompt

    # Get response from the LLM
    response = client.chat.completions.create(
        model="gemma-7b-it",
        messages=messages
    )

    assistant_response = response.choices[0].message.content
    st.session_state.chat_history.append({"role": "assistant", "content": assistant_response})

    # Display the LLM's response
    with st.chat_message("assistant"):
        st.markdown(assistant_response)
