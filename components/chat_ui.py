import streamlit as st
from services import api_client as ac

def render_chat_ui(chat_history):
    """
    Renders the chat UI and captures user input.
    """

    st.divider()
    st.header("Hi, Ashu & Ananaya! Welcome to AI Chatbot! :sunglasses:")
    user_name=ac.fetch_iam_user_name()


    #Display chat messages from history on app rerun
    #for message in st.session_state.chat_history:
        #with st.chat_message(message["role"]):
            #st.markdown(message["content"])
    
    # Display chat history
    #print("chat_history: ", chat_history)
    
    for message in chat_history:
        #print("message.type", message["role"])
        if message["role"] == "human":
            #st.markdown(f"**:male-astronaut: ** {message['role']}:** {message['content']}")
            st.markdown(f"**:male-astronaut: ** {user_name}:** {message['content']}")
        else:
            st.markdown(f":robot_face: **responsible {message['role']}:** {message['content']}")
            #st.markdown(message["content"])
    return chat_history