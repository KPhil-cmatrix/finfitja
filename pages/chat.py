"""
Developer: Khalia Phillips
App: FinFit JA
Version: 2.5
Purpose: Manages the Ask FinFit page for the FinFit JA Streamlit app.
"""

import time
import streamlit as st
from layout import show_banner, show_site_tail
from util.api_call import ask_finfit_backend

#Defining the Ask FinFit page
def open_chat():
    show_banner("Ask FinFit")
    st.markdown(
        """
        <div class="soft-card">
            <h3>Ask FinFit</h3>
            <p>Ask clear, informational questions about banking terms, account features, eligibility requirements, and general financial concepts in Jamaica. 
            This space is designed to help users better understand everyday financial/banking jargon in a simple and practical way.</p>
            <br>
            <p>Looking for tailored account suggestions instead? Use <strong>Recommendation Generator</strong>. 
            For side-by-side bank or account comparisons, use <strong>Comparison Profile</strong>.</p>
        </div>
        """,
        unsafe_allow_html=True
    )
    #Defining suggested prompts
    suggestions = [
        "What do banks actually mean by minimum opening deposit?",
        "What documents do I need to open a bank account in Jamaica?",
        "What's the difference between a savings account and a chequing account?"
    ]
    suggestion_cols = st.columns(3, gap="medium")
    for i, suggestion in enumerate(suggestions):
        with suggestion_cols[i]:
            if st.button(suggestion, key=f"chat_suggestion_{i}", use_container_width=True):
                st.session_state.pending_prompt = suggestion
    st.markdown('<div style="height:0.35rem;"></div>', unsafe_allow_html=True)
    refresh_left, refresh_mid, refresh_right = st.columns([1.2, 1, 1.2])
    with refresh_mid:
        if st.button("Start Fresh", use_container_width=True):
            st.session_state.chat_log = [
                {
                    "role": "assistant",
                    "content": (
                        "Hi there! I’m FinFit JA, and I’m here to help explain Jamaican banking terms, "
                        "account features, requirements, and general financial concepts. "
                        "Ask me anything you’d like to understand more clearly."
                    )
                }
            ]
            st.session_state.pending_prompt = None
            st.rerun()
    if "chat_log" not in st.session_state:
        st.session_state.chat_log = [
            {
                "role": "assistant",
                "content": (
                    "Hi there! I’m FinFit JA, and I’m here to help explain Jamaican banking terms, "
                    "account features, requirements, and general financial concepts. "
                    "Ask me anything you’d like to understand more clearly."
                )
            }
        ]
    if "pending_prompt" not in st.session_state:
        st.session_state.pending_prompt = None
    #Rendering chat history
    for message in st.session_state.chat_log:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])
    #Accepting user input
    user_input = st.chat_input("Ask a banking question...")
    if st.session_state.pending_prompt and not user_input:
        user_input = st.session_state.pending_prompt
        st.session_state.pending_prompt = None
    if user_input:
        st.session_state.chat_log.append({"role": "user", "content": user_input})
        with st.chat_message("user"):
            st.markdown(user_input)
        with st.chat_message("assistant"):
            with st.spinner("FinFit is thinking..."):
                time.sleep(0.8)
                try:
                    reply = ask_finfit_backend(user_input)
                except Exception:
                    reply = "Sorry, I couldn’t retrieve a response right now. Please try again in a moment."
                st.markdown(reply)
        st.session_state.chat_log.append({"role": "assistant", "content": reply})
        st.rerun()
    show_site_tail()