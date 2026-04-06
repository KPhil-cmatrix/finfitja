"""
Developer: Khalia Phillips
App: FinFit JA
Version: 1.4
Purpose: Handles API communication between the Streamlit app and the FinFit JA backend.
"""

import re
import requests
import streamlit as st

#Defining the backend request function
def ask_finfit_backend(prompt: str) -> str:
    #Retrieving secure workspace credentials from Streamlit
    base_url = st.secrets["ANYTHINGLLM_BASE_URL"].rstrip("/")
    api_key = st.secrets["ANYTHINGLLM_API_KEY"]
    workspace_slug = st.secrets["WORKSPACE_SLUG"]
    #Building the workspace chat endpoint
    url = f"{base_url}/api/v1/workspace/{workspace_slug}/chat"
    #Defining request headers
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    #Defining the request payload
    payload = {
        "message": prompt,
        "mode": "query"
    }
    #Sending the request and returning the response
    try:
        response = requests.post(url, headers=headers, json=payload, timeout=60)
        #Handling unsuccessful server responses
        if response.status_code != 200:
            return "Sorry! We seem to have run into a connection issue while trying to reach the FinFit JA model."
        data = response.json()
        #Returning the model response if available
        if data.get("textResponse"):
            raw = data["textResponse"]
            return clean_response(raw)
        #Returning a fallback message if the response is missing
        return "Sorry! The model could not generate a response right now."
    #Handling connection-related errors
    except requests.exceptions.RequestException:
        return "Sorry! We're having trouble connecting right now. Please try again shortly."

#Cleaning the model response
def clean_response(text: str) -> str:
    #Removing internal thought tags
    cleaned = re.sub(r"<think>.*?</think>", "", text, flags=re.DOTALL)
    return cleaned.strip()