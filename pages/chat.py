"""
Developer's Name: Khalia Phillips
App Name: FinFit JA
Version: 1.1
Purpose (File): This file manages the Ask FinFit page for the FinFit JA Streamlit app.
"""

import time
import streamlit as st
from layout import show_banner, show_site_tail

#Ask FinFit Chat
def open_chat():
    show_banner("Ask FinFit")
    #Keeps the page focused on informational queries
    st.caption("Use this space to ask informational questions about banking terms, account features, eligibility requirements, and general financial concepts.")
    top1, top2 = st.columns([6, 1])
    with top2:
        if st.button("↻ Refresh", use_container_width=True):
            st.session_state.chat_log = []
            st.rerun()
    #Stores the conversation for the current session
    if "chat_log" not in st.session_state:
        st.session_state.chat_log = [
            {
                "role": "assistant",
                "content": "How can I help you?"
            }
        ]
    #Shows previous messages
    for message in st.session_state.chat_log:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])
    #Handles new user input
    user_input = st.chat_input("Your message")
    if user_input:
        st.session_state.chat_log.append({"role": "user", "content": user_input})
        with st.chat_message("user"):
            st.markdown(user_input)
        with st.chat_message("assistant"):
            with st.spinner("Thinking..."):
                time.sleep(0.8)
                #Temporary placeholder response
                reply = build_placeholder_reply(user_input)
                st.markdown(reply)
        st.session_state.chat_log.append({"role": "assistant", "content": reply})
    show_site_tail()
#Temporary response block until the model call is connected
def build_placeholder_reply(user_input:str):
    return (
        f"You asked about: **{user_input}**\n\n"
        "This section is meant for informational banking questions, so the response here will focus on explanation and guidance rather than structured recommendations or comparisons."
    )
