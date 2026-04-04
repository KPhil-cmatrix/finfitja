"""
Developer: Khalia Phillips
App: FinFit JA
Version: 1.6
Purpose: Manages the Comparison Profile page.
"""

import time
import streamlit as st
from layout import show_banner, show_site_tail
from util.api_call import ask_finfit_backend

#Defining the Comparison Profile page
def open_compare():
    show_banner("Comparison Profile")
    st.markdown(
        """
        <div class="soft-card">
            <h3>Comparison Profile</h3>
            <p>Use this page to compare banks or account options side by side based on the features that matter most to you. 
            Choose the type of comparison you want, complete the form, and FinFit JA will generate a structured result for you.</p>
            <br>
            <p>Want a tailored recommendation instead? Use <strong>Recommendation Generator</strong>. 
            Need general explanations? Use <strong>Ask FinFit</strong>.</p>
        </div>
        """,
        unsafe_allow_html=True
    )
    #Creating session state for comparison results
    if "compare_result" not in st.session_state:
        st.session_state.compare_result = None
    #Creating the main two-column layout
    left_col, right_col = st.columns(2, gap="large")
    #Comparison form panel
    with left_col:
        with st.container(height=640, border=True):
            st.markdown(
                """
                <h3 style="text-align:center; margin-bottom:0.55rem;">Build Your Comparison</h3>
                <p style="margin-bottom:1rem;">Select what you would like to compare, 
                then specify what matters most in the comparison.</p>
                """,
                unsafe_allow_html=True
            )
            comparison_type = st.selectbox(
                "What would you like to compare?",
                [
                    "Banks",
                    "Accounts"
                ]
            )
            with st.form("comparison_form"):
                #Comparison setup expander
                with st.expander("Section 1: Comparison Setup", expanded=True):
                    if comparison_type == "Banks":
                        first_bank = st.selectbox(
                            "Select the first bank for comparison",
                            [
                                "NCB",
                                "Scotiabank",
                                "CIBC",
                                "First Global Bank",
                                "JN Bank",
                                "Sagicor Bank",
                                "JMMB Bank"
                            ]
                        )
                        second_bank = st.selectbox(
                            "Select the second bank for comparison",
                            [
                                "NCB",
                                "Scotiabank",
                                "CIBC",
                                "First Global Bank",
                                "JN Bank",
                                "Sagicor Bank",
                                "JMMB Bank"
                            ],
                            index=1
                        )
                    if comparison_type == "Accounts":
                        account_type = st.selectbox(
                            "Which type of account would you like to compare?",
                            [
                                "Savings",
                                "Current / Chequing",
                                "Fixed Deposit",
                                "Money Market"
                            ]
                        )
                        first_account_bank = st.selectbox(
                            "Select the first bank for comparison",
                            [
                                "NCB",
                                "Scotiabank",
                                "CIBC",
                                "JN Bank",
                                "First Global Bank",
                                "Sagicor Bank",
                                "JMMB Bank"
                            ]
                        )
                        second_account_bank = st.selectbox(
                            "Select the second bank for comparison",
                            [
                                "NCB",
                                "Scotiabank",
                                "CIBC",
                                "JN Bank",
                                "First Global Bank",
                                "Sagicor Bank",
                                "JMMB Bank"
                            ],
                            index=1
                        )
                #Comparison priorities expander
                with st.expander("Section 2: Comparison Priorities", expanded=True):
                    if comparison_type == "Banks":
                        focus_area = st.selectbox(
                            "What would you like the bank comparison to focus on?",
                            [
                                "Overall accessibility",
                                "Digital banking convenience",
                                "Branch and ATM access",
                                "Strengths and services",
                                "General side-by-side overview"
                            ]
                        )
                        user_context = st.selectbox(
                            "Which term best describes you?",
                            [
                                "Student",
                                "Employed / Salaried",
                                "Self-employed / Entrepreneur",
                                "General Customer"
                            ]
                        )
                    if comparison_type == "Accounts":
                        compare_focus = st.selectbox(
                            "What matters most to you in this account comparison?",
                            [
                                "Low fees and low entry requirements",
                                "Digital banking features",
                                "Interest and growth potential",
                                "Everyday convenience",
                                "General side-by-side overview"
                            ]
                        )
                        user_context = st.selectbox(
                            "Which term best describes you?",
                            [
                                "Student",
                                "Employed / Salaried",
                                "Self-employed / Entrepreneur",
                                "General Customer"
                            ]
                        )
                #Form buttons
                submit_col, reset_col = st.columns(2)
                with submit_col:
                    generate = st.form_submit_button("Generate Comparison", use_container_width=True)
                with reset_col:
                    reset = st.form_submit_button("Start Over", use_container_width=True)
        #Handling reset
        if reset:
            st.session_state.compare_result = None
            st.rerun()
        #Handling comparison generation
        if generate:
            if comparison_type == "Banks" and first_bank == second_bank:
                st.session_state.compare_result = "Please choose two different banks for the comparison."
                st.rerun()
            if comparison_type == "Accounts" and first_account_bank == second_account_bank:
                st.session_state.compare_result = "Please choose two different banks for the comparison."
                st.rerun()
            if comparison_type == "Banks":
                prompt = build_bank_comparison_prompt(
                    first_bank=first_bank,
                    second_bank=second_bank,
                    focus_area=focus_area,
                    user_context=user_context
                )
            if comparison_type == "Accounts":
                prompt = build_account_comparison_prompt(
                    account_type=account_type,
                    first_account_bank=first_account_bank,
                    second_account_bank=second_account_bank,
                    compare_focus=compare_focus,
                    user_context=user_context
                )
            with st.spinner("Building your comparison..."):
                time.sleep(0.8)
                try:
                    st.session_state.compare_result = ask_finfit_backend(prompt)
                except Exception:
                    st.session_state.compare_result = "Sorry, I couldn’t generate a comparison right now. Please try again in a moment."
            st.rerun()
    #Comparison output panel
    with right_col:
        with st.container(height=640, border=True):
            st.markdown(
                """
                <h3 style="text-align:center; margin-bottom:0.8rem;">Your FinFit Comparison</h3>
                """,
                unsafe_allow_html=True
            )
            if st.session_state.compare_result:
                st.markdown(st.session_state.compare_result)
            else:
                st.markdown(
                    """
                    <p style="margin-bottom:0;">Complete the form on the left, then click <strong>Generate Comparison</strong> to see your side-by-side result here.</p>
                    """,
                    unsafe_allow_html=True
                )
    show_site_tail()

#Building the bank comparison prompt
def build_bank_comparison_prompt(
    first_bank: str,
    second_bank: str,
    focus_area: str,
    user_context: str
) -> str:
    return f"""
You are FinFit JA, a Jamaican banking comparison assistant.

Compare the following two banks using the dataset only:
- First bank: {first_bank}
- Second bank: {second_bank}

User context:
- User type: {user_context}
- Comparison focus: {focus_area}

Important instructions:
- Compare only these two banks
- Use bank-level information only
- Focus on accessibility, digital services, ATM and branch access, service strengths, and general suitability
- Present the answer clearly with headings and short readable paragraphs
- End with a short summary stating which bank may be the better fit for this user context
- Do not invent information
"""

#Building the account comparison prompt
def build_account_comparison_prompt(
    account_type: str,
    first_account_bank: str,
    second_account_bank: str,
    compare_focus: str,
    user_context: str
) -> str:
    return f"""
You are FinFit JA, a Jamaican banking comparison assistant.

Compare account options from the dataset using the following profile:
- Account type to compare: {account_type}
- First bank: {first_account_bank}
- Second bank: {second_account_bank}
- User context: {user_context}
- Comparison focus: {compare_focus}

Important instructions:
- Compare relevant account options from these two banks only
- Restrict the comparison to the selected account type
- Use account-level information such as fees, opening requirements, minimum balance, debit card access, digital banking, and interest where relevant
- Present the answer clearly with headings and short readable paragraphs
- End with a short summary stating which option may be the better fit for this user context
- Do not invent account names or features
"""