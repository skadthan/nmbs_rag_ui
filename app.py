import streamlit as st
from components.chat_ui import render_chat_ui
from services.api_client import fetch_response
from utils.state_manager import initialize_state
from components.user_input import get_user_input

# Initialize session state
initialize_state()


# Page Configuration
st.set_page_config(page_title="Nimbus AI Chatbot", layout="centered")

# Render the Chat UI
st.title("Nimbus Capabilities Statement Helper")
chat_history = render_chat_ui(st.session_state['chat_history'])
#chat_history = render_chat_ui(st.session_state.chat_history)
user_message = get_user_input()

# Handle user input
if user_message:
    with st.spinner("Thinking..."):
        bot_response = fetch_response(user_message)
        # Update chat history
        st.session_state['chat_history'].append(("User", user_message))
        st.session_state['chat_history'].append(("Bot", bot_response))
