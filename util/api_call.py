"""
Developer's Name: Khalia Phillips
App Name: FinFit JA
Version: 1.0
Purpose (File): This file handles API communication between the Streamlit app and the FinFit JA backend workspace.
"""

import requests
import streamlit as st

#Defines a function to send user queries to the FinFit JA backend and retrieve responses
def ask_finfit_backend(prompt: str) -> str:
    #Retrieves secure credentials from Streamlit
    api_key = st.secrets["ANYTHINGLLM_API_KEY"]
    workspace_slug = st.secrets["ANYTHINGLLM_WORKSPACE_SLUG"]
    base_url = st.secrets["ANYTHINGLLM_BASE_URL"]
    ##Builds the workspace chat endpoint
    url = f"{base_url}/api/v1/workspace/{workspace_slug}/chat"
    #Defines request headers
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    #Defines the request payload
    payload = {
        "message": prompt,
        "mode": "query"  #Ensures responses are grounded in the dataset
    }
    #Attempts to connect to the backend and return a response
    try:
        response = requests.post(url, headers=headers, json=payload, timeout=60)
        #Handles unsuccessful responses from the server
        if response.status_code != 200:
            return "Sorry! We seem to have ran into a connection issue while trying to reach the FinFit JA model."
        data = response.json()
        #Returns the model response if available
        if data.get("textResponse"):
            return data["textResponse"].strip()
        #Fallback if a usable response is missing
        return "Sorry! The model could not generate a response right now."
    #Handles network-related errors
    except requests.exceptions.RequestException:
        return "Sorry! We're having trouble connecting right now. Please try again shortly."
