"""
Developer's Name: Khalia Phillips
App Name: FinFit JA
Version: 2.0
Purpose (File): This file manages the Ask FinFit page for the FinFit JA Streamlit app.
"""

import time
import streamlit as st
from layout import show_banner, show_site_tail
from util.api_call import ask_finfit_backend

#Defining the structure and behavior of the Ask FinFit chat interface
def open_chat():
    show_banner("Ask FinFit")
    st.error("THIS IS THE NEW CHAT PAGE")
    st.markdown(
        """
        <div class="soft-card">
            <h3>Ask FinFit</h3>
            <p>
                Use this space to ask informational questions about banking terms, account features,
                eligibility requirements, and general financial concepts in Jamaica.
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )
    control_left, control_right = st.columns([5, 1])
    with control_left:
        st.markdown(
            """
            <div class="note-box">
                <p><strong>This page is for explanations and guidance.</strong> For tailored account suggestions, use
                <strong>Recommendation Generator</strong>. For side-by-side evaluations, use
                <strong>Comparison Profile</strong>.</p>
            </div>
            """,
            unsafe_allow_html=True
        )
    with control_right:
        if st.button("↻ Refresh", use_container_width=True):
            st.session_state.chat_log = [
                {
                    "role": "assistant",
                    "content": "Hi — ask me about banking terms, account features, requirements, or financial concepts, and I’ll explain them clearly."
                }
            ]
            st.rerun()
    st.markdown('<div style="height:0.5rem;"></div>', unsafe_allow_html=True)
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
                "content": "Ask me about banking terms, account features, requirements, or financial concepts, and I’ll explain them clearly."
            }
        ]
    if "pending_prompt" not in st.session_state:
        st.session_state.pending_prompt = None
    st.markdown('<div class="chat-wrap">', unsafe_allow_html=True)
    for message in st.session_state.chat_log:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])
    st.markdown('</div>', unsafe_allow_html=True)
    user_input = st.chat_input("Ask a banking question")
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

#Temporary response block until the model call is connected
def build_placeholder_reply(user_input: str):
    return (
        f"You asked about: **{user_input}**\n\n"
        "This section is designed for informational banking questions, so responses here should focus on clear explanations, definitions, and practical guidance rather than recommendations or comparisons."
    )
