import streamlit as st
from components.chat_ui import render_chat_ui
from services.api_client import fetch_response,fetch_contextual_response
from utils.state_manager import initialize_state
from components.user_input import get_user_input

# Page Configuration
st.set_page_config(page_title="Nimbus AI Chatbot", layout="centered")

st.title("Nimbus Capabilities Statement Helper")
 # Add a divider and header
st.divider()
st.header("Hi, Ashu & Ananaya! Welcome to AI Chatbot! :sunglasses:")

# Initialize session state
initialize_state()
user_session_id="AIDAVD6I7NJDQGF3ZCQ3T"



# Render the Chat UI
render_chat_ui()

user_message = get_user_input()
print("prompt: ",user_message)

# Handle user input
if user_message:
    with st.spinner("Thinking..."):
        #bot_response = fetch_response(user_message)
        bot_response = fetch_contextual_response(user_message,user_session_id)
        # Display assistant response in chat message container
        with st.chat_message("assistant"):
            st.markdown(bot_response)
        # Update chat history
        #st.session_state['chat_history'].append(("human", user_message))
        #st.session_state['chat_history'].append(("ai", bot_response))
        st.session_state["chat_history"].append({"role": "human", "content": user_message})
        st.session_state["chat_history"].append({"role": "assistant", "content": bot_response})
