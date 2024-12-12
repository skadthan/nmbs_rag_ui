import streamlit as st
from services import api_client as ac

def get_user_input():
    """
    Renders an input field for user messages and handles user input.

    :param placeholder: The placeholder text for the input field.
    :return: The user input message if submitted, else None.
    """
    st.divider()
    user_name = ac.fetch_iam_user_name()
    #print("user_name: ", user_name)

    """
    user_message = st.text_input(
        label="Your Message:",
        placeholder=placeholder,
        key="user_input",
    ) """

    if prompt := st.chat_input("Type to talk to Claude AI Chatbot!"):
         # Display user message in chat message container
         with st.chat_message(user_name):
             st.markdown(prompt)
             # Add user message to chat history
             st.session_state.chat_history.append({"role": user_name, "content": prompt})

    #return user_message
    print("printing prompt", prompt)
    return prompt