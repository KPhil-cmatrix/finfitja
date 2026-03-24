import streamlit as st
import requests

st.set_page_config(page_title="FinFit JA", page_icon="💳", layout="centered")

# -----------------------------
# App Header
# -----------------------------
st.title("FinFit JA")
st.subheader("Your Smart Banking Assistant")
st.write("Answer a few quick questions and get a banking recommendation tailored to your needs.")

# -----------------------------
# Secrets
# -----------------------------
base_url = st.secrets["ANYTHINGLLM_BASE_URL"].rstrip("/")
api_key = st.secrets["ANYTHINGLLM_API_KEY"]
workspace_slug = st.secrets["WORKSPACE_SLUG"]

# -----------------------------
# Input Form
# -----------------------------
with st.form("finfit_form"):
    user_type = st.selectbox(
        "What best describes you?",
        ["student", "employed", "self_employed", "general"]
    )

    income = st.selectbox(
        "What is your monthly income range?",
        ["low", "medium", "high"]
    )

    goal = st.selectbox(
        "What is your main banking goal?",
        ["saving", "transactions", "investing"]
    )

    prefers_digital = st.selectbox(
        "Do you prefer digital banking?",
        ["yes", "no"]
    )

    needs_branch = st.selectbox(
        "Do you need branch access?",
        ["yes", "no"]
    )

    starting_amount = st.selectbox(
        "How much can you comfortably start with?",
        ["low", "medium", "high"]
    )

    age_group = st.selectbox(
        "What is your age group?",
        ["teen", "young_adult", "adult"]
    )

    extra_notes = st.text_area(
        "Anything else we should know?",
        placeholder="Example: I want low fees, easy online banking, and a debit card."
    )

    submitted = st.form_submit_button("Get Recommendation")

# -----------------------------
# API Call
# -----------------------------
if submitted:
    prompt = f"""
You are FinFit JA, a Jamaican banking recommendation assistant.

Use the FinFit JA workspace knowledge to recommend the most suitable bank account(s).

User profile:
- user_type: {user_type}
- monthly_income_range: {income}
- primary_goal: {goal}
- prefers_digital: {prefers_digital}
- needs_branch_access: {needs_branch}
- starting_amount: {starting_amount}
- age_group: {age_group}

Additional notes:
{extra_notes if extra_notes.strip() else "None"}

Instructions:
- Recommend 1 best option first.
- Then provide up to 2 alternatives if relevant.
- Clearly explain why each option fits.
- Focus on fees, accessibility, digital features, and suitability.
- Keep the response beginner-friendly and well-structured.
- Do not mention internal files, datasets, or backend systems.
"""

    endpoint = f"{base_url}/api/v1/workspace/{workspace_slug}/chat"
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    payload = {
        "message": prompt,
        "mode": "chat"
    }

    with st.spinner("Finding your best fit..."):
        try:
            response = requests.post(endpoint, headers=headers, json=payload, timeout=60)

            if response.status_code == 200:
                data = response.json()

                # Try common possible keys
                answer = (
                    data.get("textResponse")
                    or data.get("response")
                    or data.get("message")
                    or "Your recommendation was received, but the response format was unexpected."
                )

                st.success("Here’s your recommendation:")
                st.write(answer)

            else:
                st.error("Sorry, something went wrong while getting your recommendation.")
                st.caption(f"Error {response.status_code}")

        except Exception:
            st.error("We couldn't connect to the recommendation service right now. Please try again.")
