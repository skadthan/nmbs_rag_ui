import requests

API_BASE_URL = "http://localhost:8000/nmbs/api"  # Replace with your backend URL

def fetch_response(user_query,refresh_token):
    """
    Sends the user's message to the backend API and retrieves the chatbot's response.
    """
    try:
        headers = {
            "Authorization": f"Bearer {refresh_token}",
            "Content-Type": "application/json"
        }
        response = requests.post(f"{API_BASE_URL}/chat/ask", json={"query": user_query},headers=headers)
        response.raise_for_status()
        return response.json().get("aiResponse", "I'm sorry, something went wrong.")
    except requests.RequestException as e:
        return "Error connecting to the chatbot API. Please try again later."
    

def fetch_contextual_response(user_query,user_session_id, refresh_token):
    """
    Sends the user's message to the backend API and retrieves the chatbot's response.
    """
    try:
        headers = {
            "Authorization": f"Bearer {refresh_token}",
            "Content-Type": "application/json"
        }
        response = requests.post(f"{API_BASE_URL}/chat/contextualbot", json={"session_id": user_session_id, "query": user_query},headers=headers)
        response.raise_for_status()
        #return response.json().get("aiResponse", "I'm sorry, something went wrong.")
        return response
    except requests.RequestException as e:
        print('Exception - fetch_contextual_response: ',e)
        return "Error connecting to the chatbot API. Please try again later."

def fetch_chat_history(user_session_id,refresh_token):
    """
    Get's the chat history from DynamoDB Session Table.

    """
    try:
        # Set the headers with the bearer token
        headers = {
            "Authorization": f"Bearer {refresh_token}",
            "Content-Type": "application/json"
        }
        response = requests.post(f"{API_BASE_URL}/session/getchathistory", json={"user_session_id": user_session_id},headers=headers)
        response.raise_for_status()
        return response.json().get("messages", "I'm sorry, something went wrong.")
    except requests.RequestException as e:
        return "Error connecting to the chatbot API. Please try again later."

def fetch_iam_user_id(refresh_token):
    """
    Get's the IAM user ID.

    """
    try:
         # Set the headers with the bearer token
        headers = {
            "Authorization": f"Bearer {refresh_token}",
            "Content-Type": "application/json"
        }
        response = requests.get(f"{API_BASE_URL}/iam/getiamuserid",headers=headers)
        print("getiamuserid: ", response.get("iam_id"))
        response.raise_for_status()
        return response.json().get("iam_id", "I'm sorry, something went wrong.")
    except requests.RequestException as e:
        return "Error connecting to the chatbot API. Please try again later."


def fetch_iam_user_name(refresh_token):
    """
    Get's the IAM user name.

    """
    try:
        headers = {
            "Authorization": f"Bearer {refresh_token}",
            "Content-Type": "application/json"
        }
        response = requests.get(f"{API_BASE_URL}/iam/getiamusername",headers=headers)
        response.raise_for_status()
        return response.json().get("iam_username", "I'm sorry, something went wrong.")
    except requests.RequestException as e:
        return "Error connecting to the chatbot API. Please try again later."
    

def fetch_authenticate(username, password):
    """
    Authenticate Nimbus user credentials.

    """
    try:
        response = requests.post(f"{API_BASE_URL}/auth/login",json={"username": username, "password": password})
        response.raise_for_status()
        #refresh_token = response.json().get("refresh_token")
        return response.json().get("refresh_token", "I'm sorry, something went wrong.")
    except requests.RequestException as e:
        return "Error connecting to the chatbot API. Please try again later."
