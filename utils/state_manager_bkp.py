import streamlit as st
from services import api_client as ac

def initialize_state():
    """
    Initializes the session state variables.
    """

    user_session_id="AIDAVD6I7NJDQGF3ZCQ3T"
    # Use a flag to ensure the function runs only once
    if "initialized" in st.session_state:
        return  # Skip initialization if already done

    # Ensure "chat_history" key is initialized
    if "chat_history" not in st.session_state:
        print("Initializing chat_history")
        st.session_state["chat_history"] = []  # Initialize as an empty list

    # Fetch stored messages from the backend only if chat_history is empty
    if not st.session_state["chat_history"]:
        print("if not st.session_state.chat_history")
        stored_messages = []
        try:
            stored_messages = ac.fetch_chat_history(user_session_id=user_session_id)
            #print("\nstored_messages\n",stored_messages)
        except Exception as e:
            print(f"Error fetching chat history: {e}")
        

        # Populate the session state with the retrieved messages
        for msg in stored_messages:
            role = msg.get("type", "unknown")  # Default to "unknown" if 'type' is missing
            content = msg.get("content", "")   # Default to an empty string if 'content' is missing
            st.session_state["chat_history"].append({"role": role, "content": content})
    
    st.session_state["initialized"] = True  # Set the flag
    #print("Session state keys:", st.session_state.keys())
    #print("Chat history initialized:", st.session_state["chat_history"])