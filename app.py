import streamlit as st
import requests
st.set_page_config(page_title="FinFit JA", page_icon="💳")
st.title("FinFit JA")
st.subheader("Backend Connection Test")
base_url = st.secrets["ANYTHINGLLM_BASE_URL"]
api_key = st.secrets["ANYTHINGLLM_API_KEY"]
workspace_slug = st.secrets["WORKSPACE_SLUG"]
st.write("Click the button below to test the connection to AnythingLLM.")
if st.button("Test Backend Connection"):
    endpoint = f"{base_url}/api/v1/workspace/{workspace_slug}/chat"
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    payload = {
        "message": "Hello. Give me a short test reply from the FinFit JA workspace.",
        "mode": "chat"
    }
    try:
        response = requests.post(endpoint, headers=headers, json=payload, timeout=60)
        st.write("Status Code:", response.status_code)
        if response.status_code == 200:
            data = response.json()
            st.success("Connection successful!")
            st.write("Raw response:")
            st.json(data)
        else:
            st.error("Connection failed.")
            st.text(response.text)
    except Exception as e:
        st.error(f"An error occurred: {e}")
