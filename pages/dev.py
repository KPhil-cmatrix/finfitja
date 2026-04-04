"""
Developer: Khalia Phillips
App: FinFit JA
Version: 1.5
Purpose: Manages the Development Overview page.
"""

import streamlit as st
from layout import show_banner, show_site_tail

#Defining the Development Overview page
def open_build():
    show_banner("Development Overview")
    st.markdown(
        """
        <div class="soft-card">
            <h3>Development Process</h3>
            <p>This section outlines the overall approach used to build FinFit JA, including the main development stages, implementation decisions, and refinements made throughout the project.</p>
        </div>
        """,
        unsafe_allow_html=True
    )
    #Development stages row one
    process_cols_1 = st.columns(3, gap="medium")
    with process_cols_1[0]:
        with st.expander("1. Data Collection", expanded=False):
            st.markdown(
                """
                Banking data was collected from seven (7) major commercial banks in Jamaica, with an emphasis on similar account types and their fees, features, and requirements. 
                Information was verified using official bank sources to improve accuracy and consistency across the system.
                """
            )
    with process_cols_1[1]:
        with st.expander("2. Data Structuring", expanded=False):
            st.markdown(
                """
                The collected information was sanitized, standardized, and organized into several structured Markdown datasets. 
                This made it easier for the model to retrieve, interpret, and apply relevant financial product information consistently.
                """
            )
    with process_cols_1[2]:
        with st.expander("3. Decision Logic", expanded=False):
            st.markdown(
                """
                A rule-based decision logic layer was developed to map user needs to product features. 
                This allowed the system to evaluate user intent, rank suitable options, and generate recommendations with supporting explanations.
                """
            )
    #Development stages row two
    process_cols_2 = st.columns(3, gap="medium")
    with process_cols_2[0]:
        with st.expander("4. System Integration", expanded=False):
            st.markdown(
                """
                The datasets were integrated into an AnythingLLM workspace, while the GPT model was connected through an OpenRouter API Key. 
                Retrieval-Augmented Generation was used to improve contextual accuracy by retrieving relevant dataset information first.
                """
            )
    with process_cols_2[1]:
        with st.expander("5. Interface Development", expanded=False):
            st.markdown(
                """
                A Streamlit-based web interface was developed to make the system accessible and easy to use. 
                The interface supports informational queries, recommendations, and comparisons in a clean and structured format.
                """
            )
    with process_cols_2[2]:
        with st.expander("6. Testing and Refinement", expanded=False):
            st.markdown(
                """
                The system was continuously tested using sample users and different query types to assess accuracy, relevance, and usability. 
                Based on the findings, datasets, prompts, and system settings were refined for better consistency and clarity.
                """
            )
    st.markdown('<hr class="soft-divider">', unsafe_allow_html=True)
    st.markdown(
        """
        <div class="soft-card">
            <h3>Major Challenges and Solutions</h3>
            <p>Several technical and functional challenges emerged throughout development. 
            These issues were addressed through structured design decisions, testing, and continuous refinement.</p>
        </div>
        """,
        unsafe_allow_html=True
    )
    #Challenge cards row one
    challenge_cols_1 = st.columns(2, gap="medium")
    with challenge_cols_1[0]:
        with st.expander("Challenge: Data Inconsistency", expanded=False):
            st.markdown(
                """
                **Solution:**  
                Financial data from different banks varied in terminology, formatting, and level of detail. 
                This was addressed by cleaning, standardizing, and reorganizing the data into a unified structure supported by predefined tags and consistent dataset formatting.
                """
            )
    with challenge_cols_1[1]:
        with st.expander("Challenge: User Intent Interpretation", expanded=False):
            st.markdown(
                """
                **Solution:**  
                The system handled clear queries well, but vague or indirect inputs were harder to interpret. 
                A decision logic framework was introduced to map user inputs to predefined tags and improve response relevance through structured matching.
                """
            )
    #Challenge cards row two
    challenge_cols_2 = st.columns(2, gap="medium")
    with challenge_cols_2[0]:
        with st.expander("Challenge: Response Quality and Performance", expanded=False):
            st.markdown(
                """
                **Solution:**  
                Early outputs were sometimes inconsistent or too long. 
                This was improved by refining model configurations and optimizing the system prompt to produce clearer, shorter, and more structured responses for users.
                """
            )
    with challenge_cols_2[1]:
        with st.expander("Challenge: Security and Reliability", expanded=False):
            st.markdown(
                """
                **Solution:**  
                Prompt injection and attempts to access restricted information were considered during testing. 
                System-level constraints were added to keep responses limited to dataset-driven content and preserve safe, intended behavior.
                """
            )
    show_site_tail()