"""
Developer's Name: Khalia Phillips
App Name: FinFit JA
Version: 1.0
Purpose (File): This file handles API communication between the Streamlit app and the FinFit JA backend workspace.
"""

import requests
import streamlit as st


# Function: Ask FinFit Backend
def ask_finfit_backend(prompt: str) -> str:
    """
    Sends a user query to the FinFit JA workspace and retrieves a response.

    Parameters:
    prompt (str): The user's input message

    Returns:
    str: A clean response from the model or an error message if the request fails
    """

    #Retrieves secure credentials stored in Streamlit secrets
    api_key = st.secrets["ANYTHINGLLM_API_KEY"]
    workspace_slug = st.secrets["ANYTHINGLLM_WORKSPACE_SLUG"]
    base_url = st.secrets["ANYTHINGLLM_BASE_URL"]


    #Constructs the API endpoint
    url = f"{base_url}/api/v1/workspace/{workspace_slug}/chat"

    #Defines headers for authentication and content type
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }

    #Defines the payload sent to the model
    payload = {
        "message": prompt,
        "mode": "query"  #Ensures responses are grounded in the dataset
    }


    #Attempts to send request to backend
    try:
        response = requests.post(url, headers=headers, json=payload, timeout=60)

        #Handles unsuccessful response from the server
        if response.status_code != 200:
            return "Sorry — I ran into a connection issue while trying to reach FinFit."

        data = response.json()

        #Extracts and returns the model's response
        return data.get(
            "textResponse",
            "Sorry — I couldn’t generate a response right now."
        )


    #Handles network-related errors
    except requests.exceptions.RequestException:
        return "Sorry — I’m having trouble connecting right now. Please try again shortly."
