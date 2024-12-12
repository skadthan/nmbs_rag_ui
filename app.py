import streamlit as st
from components.chat_ui import render_chat_ui
from services.api_client import fetch_response, fetch_contextual_response, fetch_authenticate
from utils.state_manager import initialize_state
from components.user_input import get_user_input

# Page Configuration
st.set_page_config(page_title="Nimbus AI Chatbot", layout="centered")

# User session identifier (you can replace this with dynamic data)
user_session_id = "AIDAVD6I7NJDQGF3ZCQ3T"

# Simulated valid user credentials
VALID_USERS = {
    "admin": "password123",
    "skadthan": "userpassword",
}

def login_ui():
    """
    Renders the login UI and handles authentication logic.
    """
    st.title("Welcome to Nimbus Consulting")

    # If user is already logged in, skip login form
    if "logged_in" in st.session_state and st.session_state.logged_in:
        print("in login_ui: loggged_in is in session_state")
        return True

    # Display the login form
    st.subheader("Please log in to continue")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    # Login button
    if st.button("Login"):
        #if username in VALID_USERS and VALID_USERS[username] == password:
        if username in VALID_USERS:
            try:
                refresh_token = fetch_authenticate(username, password)
                if "Error " not in refresh_token:
                    st.session_state.refresh_token = refresh_token
                    print("refresh_token",refresh_token)
                    st.session_state.logged_in = True
                    st.session_state.username = username
                    st.success("Login successful!")
                    #ui_router()
                else:
                    st.session_state.logged_in = False
                    st.error("Login is not successful!")
                    

            except Exception as e:
                st.error(f"Login failed: {str(e)}") 
        else:
            st.error("Invalid username or password. Please try again.")

    return False

def chatbot_ui(user_name, refresh_token):
    """
    Renders the chatbot UI.
    """
    st.title("Nimbus Capabilities Statement Helper")
    # Add a divider and header
    st.divider()
    st.header(f"Hi, {st.session_state.username}! Welcome to AI Chatbot! :sunglasses:")

    # Initialize session state
    user_session_id=user_name
    user_session_id="AIDAVD6I7NJDQGF3ZCQ3T"
    initialize_state(user_session_id,refresh_token)

    # Render the Chat UI
    render_chat_ui(refresh_token)

    user_message = get_user_input(refresh_token)
    print("prompt: ", user_message)

    # Handle user input
    if user_message:
        with st.spinner("Thinking..."):
            # Fetch the bot's response
            bot_response = fetch_contextual_response(user_message, user_session_id,refresh_token)

            # Display assistant response in chat message container
            with st.chat_message("assistant"):
                st.markdown(bot_response)

            # Update chat history
            st.session_state["chat_history"].append({"role": "human", "content": user_message})
            st.session_state["chat_history"].append({"role": "assistant", "content": bot_response})
    
    if st.button("Logout"):
        st.session_state.logged_in = False
        st.session_state.username = None  # Clear the username on logout

def ui_router():
    login_count=0
    if st.session_state.logged_in:
        print("Routing to Chatbot UI")
        chatbot_ui(st.session_state.username, st.session_state.refresh_token)
    else:
        login_count=login_count+1
        print(f"Routing to Login UI count- {login_count}")
        login_ui()

# Main app logic
def main():
    """
    Main function to display content.
    """
    print("Main function to display content.")
    
    if "logged_in" not in st.session_state:
        print("logged_in is not in session_sate")
        st.session_state.logged_in = False
    
    ui_router()

if __name__ == "__main__":
    main()
