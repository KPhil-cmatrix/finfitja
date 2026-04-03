"""
Developer's Name: Khalia Phillips
App Name: FinFit JA
Version: 3.0
Purpose (File): This file manages the Ask FinFit page for the FinFit JA Streamlit app.
"""

import time
import streamlit as st
from layout import show_banner, show_site_tail
from util.api_call import ask_finfit_backend

# Defining the structure and behavior of the Ask FinFit chat interface
def open_chat():
    show_banner("Ask FinFit")
    st.markdown(
        """
        <div class="soft-card">
            <h3>Ask FinFit</h3>
            <p>
                Ask clear, informational questions about banking terms, account features,
                eligibility requirements, and general financial concepts in Jamaica.
                This space is designed to help users better understand banking options,
                requirements, and everyday financial language in a simple, practical way.
                <br>
                Looking for tailored account suggestions? Use<strong>Recommendation Generator</strong>.
                For side-by-side account evaluations, use <strong>Comparison Profile</strong>.
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )
    top_left, top_right = st.columns([5, 1])
    with top_right:
        if st.button("↻ Refresh Chat", use_container_width=True):
            st.session_state.chat_log = [
                {
                    "role": "assistant",
                    "content": (
                        "Hi there! I’m FinFit JA and I'm here to help explain Jamaican banking terms,"
                        " account features, requirements, and general financial concepts."
                        " Ask me anything you’d like to understand more clearly."
                    )
                }
            ]
            st.session_state.pending_prompt = None
            st.rerun()
    suggestion_cols = st.columns(3, gap="medium")
    suggestions = [
        "What do banks mean by minimum opening deposit?",
        "What documents do I usually need to open a bank account in Jamaica?",
        "What is the difference between a savings account and a chequing account?"
    ]
    for i, suggestion in enumerate(suggestions):
        with suggestion_cols[i]:
            if st.button(suggestion, key=f"chat_suggestion_{i}", use_container_width=True):
                st.session_state.pending_prompt = suggestion
    if "chat_log" not in st.session_state:
        st.session_state.chat_log = [
            {
                "role": "assistant",
                "content": (
                    "Hi there. I’m FinFit JA and I'm here to help explain Jamaican banking terms,"
                    " account features, requirements, and general financial concepts."
                    " Ask me anything you’d like to understand more clearly."
                )
            }
        ]
    if "pending_prompt" not in st.session_state:
        st.session_state.pending_prompt = None
    for message in st.session_state.chat_log:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])
    user_input = st.chat_input("What can I help you understand about banking in Jamaica today?")
    if st.session_state.pending_prompt and not user_input:
        user_input = st.session_state.pending_prompt
        st.session_state.pending_prompt = None
    if user_input:
        st.session_state.chat_log.append({"role": "user", "content": user_input})
        with st.chat_message("user"):
            st.markdown(user_input)
        with st.chat_message("assistant"):
            with st.spinner("Thinking..."):
                time.sleep(0.8)
                try:
                    reply = ask_finfit_backend(user_input)
                except Exception:
                    reply = build_placeholder_reply(user_input)

                st.markdown(reply)
        st.session_state.chat_log.append({"role": "assistant", "content": reply})
        st.rerun()
    show_site_tail()


# Temporary response block until the model call is connected
def build_placeholder_reply(user_input: str):
    return (
        f"I’m not fully connected to the live workspace yet, so here’s a placeholder response for: **{user_input}**.\n\n"
        "Once the backend connection is active, this page will return real informational answers from the FinFit JA workspace instead of fallback text."
    )