import requests

API_BASE_URL = "http://localhost:8000/nmbs/api"  # Replace with your backend URL

def fetch_response(user_query):
    """
    Sends the user's message to the backend API and retrieves the chatbot's response.
    """
    try:
        response = requests.post(f"{API_BASE_URL}/chat/ask", json={"query": user_query})
        response.raise_for_status()
        return response.json().get("aiResponse", "I'm sorry, something went wrong.")
    except requests.RequestException as e:
        return "Error connecting to the chatbot API. Please try again later."
    

def fetch_chat_history(user_session_id):
    """
    Get's the chat history from DynamoDB Session Table.

    """
    try:
        response = requests.post(f"{API_BASE_URL}/session/getchathistory", json={"user_session_id": user_session_id})
        response.raise_for_status()
        return response.json().get("messages", "I'm sorry, something went wrong.")
    except requests.RequestException as e:
        return "Error connecting to the chatbot API. Please try again later."

def fetch_iam_user_id():
    """
    Get's the IAM user ID.

    """
    try:
        response = requests.get(f"{API_BASE_URL}/iam/getiamuserid")
        print("getiamuserid: ", response.get("iam_id"))
        response.raise_for_status()
        return response.json().get("iam_id", "I'm sorry, something went wrong.")
    except requests.RequestException as e:
        return "Error connecting to the chatbot API. Please try again later."


def fetch_iam_user_name():
    """
    Get's the IAM user name.

    """
    try:
        response = requests.get(f"{API_BASE_URL}/iam/getiamusername")
        response.raise_for_status()
        return response.json().get("iam_username", "I'm sorry, something went wrong.")
    except requests.RequestException as e:
        return "Error connecting to the chatbot API. Please try again later."
