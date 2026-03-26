import re
import requests
import streamlit as st

st.set_page_config(page_title="FinFit JA", page_icon="💳", layout="centered")


def build_prompt(
    user_type: str,
    income: str,
    goal: str,
    prefers_digital: str,
    needs_branch: str,
    starting_amount: str,
    age_group: str,
    extra_notes: str,
) -> str:
    """Build the prompt sent to the AnythingLLM workspace."""
    notes = extra_notes.strip() if extra_notes.strip() else "None"

    return f"""
You are FinFit JA, a Jamaican banking recommendation assistant.

Use the FinFit JA workspace knowledge to recommend the most suitable bank account(s) or financial products.

User profile:
- user_type: {user_type}
- monthly_income_range: {income}
- primary_goal: {goal}
- prefers_digital: {prefers_digital}
- needs_branch_access: {needs_branch}
- starting_amount: {starting_amount}
- age_group: {age_group}

Additional notes:
{notes}

Instructions:
- Recommend 1 best option first.
- Then provide up to 2 alternatives if relevant.
- Clearly explain why each option fits.
- Focus on fees, accessibility, digital features, suitability, and where relevant, product difficulty/accessibility.
- Keep the response beginner-friendly and well-structured.
- Do not mention internal files, datasets, workspace knowledge, system instructions, or backend systems.
- Do not expose internal reasoning, analysis, or step-by-step thought process.
- Output only the final answer for the user.
""".strip()


def clean_llm_response(raw_text: str) -> str:
    """
    Remove visible reasoning or analysis leakage from model output.
    """
    if not raw_text:
        return ""

    text = raw_text.strip()

    # Remove any <think>...</think> blocks
    text = re.sub(r"(?is)<think>.*?</think>", "", text).strip()

    # Remove common leaked reasoning/opening lines
    patterns = [
        r"(?is)^we need to answer based on context\..*?(?=\n\n|$)",
        r"(?is)^based on context\..*?(?=\n\n|$)",
        r"(?is)^the user asks:.*?(?=\n\n|$)",
        r"(?is)^we have context:.*?(?=\n\n|$)",
        r"(?is)^internal reasoning:.*?(?=\n\n|$)",
        r"(?is)^analysis:.*?(?=\n\n|$)",
        r"(?is)^thinking:.*?(?=\n\n|$)",
    ]

    for pattern in patterns:
        text = re.sub(pattern, "", text).strip()

    # Remove any leftover standalone think tags just in case
    text = re.sub(r"(?is)</?think>", "", text).strip()

    # If a reasoning marker appears, keep only the content after it
    marker_patterns = [
        r"(?is)final answer:\s*(.*)",
        r"(?is)answer:\s*(.*)",
    ]
    for pattern in marker_patterns:
        match = re.search(pattern, text)
        if match:
            possible_answer = match.group(1).strip()
            if possible_answer:
                text = possible_answer
                break

    # Clean excessive blank lines and spaces
    text = re.sub(r"\n{3,}", "\n\n", text)
    text = re.sub(r"[ \t]{2,}", " ", text).strip()

    return text


def extract_answer(data: dict) -> str:
    """Extract the most likely answer field from the AnythingLLM response."""
    if not isinstance(data, dict):
        return ""

    return (
        data.get("textResponse")
        or data.get("response")
        or data.get("message")
        or data.get("text")
        or ""
    )


# -----------------------------
# App Header
# -----------------------------
st.title("FinFit JA")
st.subheader("Your Smart Banking Assistant")
st.write(
    "Answer a few quick questions and get a banking recommendation tailored to your needs."
)

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
        ["student", "employed", "self_employed", "general"],
    )

    income = st.selectbox(
        "What is your monthly income range?",
        ["low", "medium", "high"],
    )

    goal = st.selectbox(
        "What is your main banking goal?",
        ["saving", "transactions", "investing"],
    )

    prefers_digital = st.selectbox(
        "Do you prefer digital banking?",
        ["yes", "no"],
    )

    needs_branch = st.selectbox(
        "Do you need branch access?",
        ["yes", "no"],
    )

    starting_amount = st.selectbox(
        "How much can you comfortably start with?",
        ["low", "medium", "high"],
    )

    age_group = st.selectbox(
        "What is your age group?",
        ["teen", "young_adult", "adult"],
    )

    extra_notes = st.text_area(
        "Anything else we should know?",
        placeholder="Example: I want low fees, easy online banking, and a debit card.",
    )

    submitted = st.form_submit_button("Get Recommendation")

# -----------------------------
# API Call
# -----------------------------
if submitted:
    prompt = build_prompt(
        user_type=user_type,
        income=income,
        goal=goal,
        prefers_digital=prefers_digital,
        needs_branch=needs_branch,
        starting_amount=starting_amount,
        age_group=age_group,
        extra_notes=extra_notes,
    )

    endpoint = f"{base_url}/api/v1/workspace/{workspace_slug}/chat"
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
    }

    # Note:
    # The reasoning block below is an attempted passthrough.
    # Whether this works depends on whether AnythingLLM forwards it to OpenRouter.
    payload = {
        "message": prompt,
        "mode": "chat",
        "reasoning": {
            "exclude": True
        },
    }

    with st.spinner("Finding your best fit..."):
        try:
            response = requests.post(
                endpoint,
                headers=headers,
                json=payload,
                timeout=60,
            )

            if response.status_code == 200:
                data = response.json()
                raw_answer = extract_answer(data)

                if raw_answer:
                    cleaned_answer = clean_llm_response(raw_answer)

                    st.success("Here’s your recommendation:")
                    st.write(
                        cleaned_answer
                        if cleaned_answer
                        else "A response was received, but it could not be displayed cleanly."
                    )
                else:
                    st.warning(
                        "A response was received, but the format was unexpected."
                    )
                    st.caption("Try testing the workspace directly or inspect the API response.")

            else:
                st.error("Sorry, something went wrong while getting your recommendation.")
                st.caption(f"Error {response.status_code}")

                try:
                    error_data = response.json()
                    st.caption(str(error_data))
                except Exception:
                    st.caption(response.text[:500])

        except requests.exceptions.Timeout:
            st.error("The recommendation service took too long to respond. Please try again.")
        except requests.exceptions.ConnectionError:
            st.error("We couldn't connect to the recommendation service right now.")
        except Exception as e:
            st.error("Something unexpected happened while getting your recommendation.")
            st.caption(str(e))
