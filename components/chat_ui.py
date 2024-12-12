import streamlit as st
from services import api_client as ac

def render_chat_ui():
    """
    Renders the full chat UI and appends new messages dynamically.
    """
    user_name = ac.fetch_iam_user_name()

    # Ensure session state has 'last_rendered_index' to track rendered messages
    if "last_rendered_index" not in st.session_state:
        st.session_state["last_rendered_index"] = 0

    # Get the chat history from session state
    chat_history = st.session_state["chat_history"]

    # Render all messages up to the last rendered index (preserve old messages)
    for idx in range(st.session_state["last_rendered_index"]):
        message = chat_history[idx]
        if message["role"] == "human":
            with st.chat_message("human"):
                st.markdown(f"**:male-astronaut: {user_name}:** {message['content']}")
        else:
            with st.chat_message("assistant"):
                st.markdown(f":robot_face: **Assistant:** {message['content']}")

    # Render only new messages (dynamically append)
    for idx in range(st.session_state["last_rendered_index"], len(chat_history)):
        message = chat_history[idx]
        if message["role"] == "human":
            with st.chat_message("human"):
                st.markdown(f"**:male-astronaut: {user_name}:** {message['content']}")
        else:
            with st.chat_message("assistant"):
                st.markdown(f":robot_face: **Assistant:** {message['content']}")

    # Update last rendered index to the current history length
    st.session_state["last_rendered_index"] = len(chat_history)

    return chat_history
