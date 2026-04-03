"""
Developer's Name: Khalia Phillips
App Name: FinFit JA
Version: 1.0
Purpose (File): This file manages the Recommendation Generator page for the FinFit JA Streamlit app.
"""

import time
import streamlit as st
from layout import show_banner, show_site_tail
from util.api_call import ask_finfit_backend


#Recommendation Generator Page
def open_matcher():
    show_banner("Recommendation Generator")

    st.markdown(
        """
        <div class="soft-card">
            <h3>Recommendation Generator</h3>
            <p>
                Use this page to generate a tailored bank account recommendation based on your profile,
                needs, and preferences. Start by choosing the option that best describes you, then tell
                FinFit JA what matters most to you.
                <br><br>
                Need general explanations instead? Use <strong>Ask FinFit</strong>.
                Want to compare bank or account options side by side? Use <strong>Comparison Profile</strong>.
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )

    #Creates state values for recommendation handling
    if "matcher_result" not in st.session_state:
        st.session_state.matcher_result = None

    #Creates the main two-column layout
    left_col, right_col = st.columns(2, gap="large")

    #Left Side - User Form
    with left_col:
        with st.container(height=640, border=True):
            st.markdown(
                """
                <h3 style="text-align:center; margin-bottom:0.55rem;">Tell FinFit About You</h3>
                <p style="margin-bottom:1rem;">
                    Answer a few quick questions so I can recommend the best-fit account for your needs.
                </p>
                """,
                unsafe_allow_html=True
            )

            with st.form("recommendation_form"):
                #Section 1 - Basic Profile
                with st.expander("Section 1: About You", expanded=True):
                    user_type = st.selectbox(
                        "Which best describes you?",
                        [
                            "Student",
                            "Employed / salaried",
                            "Self-employed / business-minded",
                            "General customer"
                        ]
                    )

                    age_group = st.selectbox(
                        "Which age group are you in?",
                        [
                            "Teen",
                            "Young adult",
                            "Adult"
                        ]
                    )

                    primary_goal = st.selectbox(
                        "What are you mainly looking for right now?",
                        [
                            "Save money",
                            "Manage everyday spending",
                            "Grow money over time",
                            "Start with a simple account"
                        ]
                    )

                    monthly_income = st.selectbox(
                        "Which income range best fits you right now?",
                        [
                            "Lower income",
                            "Moderate income",
                            "Higher income"
                        ]
                    )

                    starting_amount = st.selectbox(
                        "How much would you be comfortable starting with?",
                        [
                            "A small amount",
                            "A moderate amount",
                            "A larger amount"
                        ]
                    )

                #Section 2 - Preferences
                with st.expander("Section 2: Your Preferences", expanded=True):
                    low_fee_priority = st.radio(
                        "How important are low or no monthly fees to you?",
                        [
                            "Very important",
                            "Somewhat important",
                            "Not a priority"
                        ]
                    )

                    digital_preference = st.radio(
                        "Do you want to do most of your banking online?",
                        [
                            "Yes, definitely",
                            "A mix of online and in-person is fine",
                            "No, I prefer going into the bank"
                        ]
                    )

                    access_importance = st.radio(
                        "Will easy access to branches and ATMs matter to you?",
                        [
                            "Yes, very important",
                            "Nice to have",
                            "Not really"
                        ]
                    )

                    interest_preference = st.radio(
                        "Would you like your money to earn interest if possible?",
                        [
                            "Yes",
                            "Not necessary"
                        ]
                    )

                    extras = st.multiselect(
                        "Anything else that matters to you? (Optional)",
                        [
                            "I want a debit card",
                            "I want low opening requirements",
                            "I want strong digital banking",
                            "I want easy branch and ATM access",
                            "I want something mainly for saving",
                            "I want something mainly for everyday transactions"
                        ]
                    )

                #Form Buttons
                submit_col, reset_col = st.columns(2)

                with submit_col:
                    generate = st.form_submit_button("Generate Recommendation", use_container_width=True)

                with reset_col:
                    reset = st.form_submit_button("Start Over", use_container_width=True)

        #Handles Reset
        if reset:
            st.session_state.matcher_result = None
            st.rerun()

        #Handles Recommendation Generation
        if generate:
            prompt = build_recommendation_prompt(
                user_type=user_type,
                age_group=age_group,
                primary_goal=primary_goal,
                monthly_income=monthly_income,
                starting_amount=starting_amount,
                low_fee_priority=low_fee_priority,
                digital_preference=digital_preference,
                access_importance=access_importance,
                interest_preference=interest_preference,
                extras=extras
            )

            with st.spinner("Generating your FinFit match..."):
                time.sleep(0.8)
                try:
                    st.session_state.matcher_result = ask_finfit_backend(prompt)
                except Exception:
                    st.session_state.matcher_result = (
                        "Sorry — I couldn’t generate a recommendation right now. "
                        "Please try again in a moment."
                    )

            st.rerun()

    #Right Side - Recommendation Output
    with right_col:
        with st.container(height=640, border=True):
            st.markdown(
                """
                <h3 style="text-align:center; margin-bottom:0.8rem;">Your FinFit Match</h3>
                """,
                unsafe_allow_html=True
            )

            if st.session_state.matcher_result:
                st.markdown(st.session_state.matcher_result)
            else:
                st.markdown(
                    """
                    <p style="margin-bottom:0;">
                        Complete the questions on the left, then click
                        <strong>Generate Recommendation</strong>
                        to see your best-fit account here.
                    </p>
                    """,
                    unsafe_allow_html=True
                )

    show_site_tail()


#Builds a structured prompt from the user's selections
def build_recommendation_prompt(
    user_type: str,
    age_group: str,
    primary_goal: str,
    monthly_income: str,
    starting_amount: str,
    low_fee_priority: str,
    digital_preference: str,
    access_importance: str,
    interest_preference: str,
    extras: list[str]
) -> str:
    #Creates a cleaner version of optional preferences
    extras_text = ", ".join(extras) if extras else "No additional preferences provided."

    return f"""
You are FinFit JA, a Jamaican banking recommendation assistant.

Use the user's profile below to recommend the most suitable bank account from the dataset.

Give:
1. One best-fit account recommendation
2. One or two alternative options if relevant
3. A short explanation of why the recommendation fits
4. Key features the user should notice
5. A brief note on any limitation or trade-off

Keep the response user-friendly, practical, and tailored.

User profile:
- User type: {user_type}
- Age group: {age_group}
- Primary goal: {primary_goal}
- Income range: {monthly_income}
- Starting amount: {starting_amount}
- Importance of low or no monthly fees: {low_fee_priority}
- Digital banking preference: {digital_preference}
- Need for branch and ATM access: {access_importance}
- Interest preference: {interest_preference}
- Extra preferences: {extras_text}

Important instructions:
- Recommend specific account names from the dataset only
- Match the user to the most suitable option based on needs and preferences
- Do not invent products
- Present the answer clearly with headings and short, readable paragraphs
"""