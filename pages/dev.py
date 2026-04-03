"""
Developer's Name: Khalia Phillips
App Name: FinFit JA
Version: 1.2
Purpose (File): This file manages the Dev Process page for the FinFit JA Streamlit app.
"""

import streamlit as st
from layout import show_banner, show_site_tail


#Dev Process Page
def open_build():
    show_banner("Dev Process")

    st.markdown(
        """
        <div class="soft-card">
            <h3>Development Process</h3>
            <p>
                This section outlines the overall development approach used to build FinFit JA,
                including the main implementation stages and the improvements made throughout the project.
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )

    process_cols_1 = st.columns(3, gap="medium")

    with process_cols_1[0]:
        st.markdown(
            """
            <div class="mini-card">
                <h3>1. Data Collection</h3>
                <p>
                    Banking data was collected from seven major commercial banks in Jamaica,
                    with emphasis on account types, fees, features, and requirements.
                    Information was verified using official bank sources to improve accuracy
                    and consistency across the system.
                </p>
            </div>
            """,
            unsafe_allow_html=True
        )

    with process_cols_1[1]:
        st.markdown(
            """
            <div class="mini-card">
                <h3>2. Data Structuring</h3>
                <p>
                    The collected information was cleaned, standardized, and organized into
                    structured Markdown datasets. This made it easier for the model to retrieve,
                    interpret, and apply relevant financial product information consistently.
                </p>
            </div>
            """,
            unsafe_allow_html=True
        )

    with process_cols_1[2]:
        st.markdown(
            """
            <div class="mini-card">
                <h3>3. Decision Logic</h3>
                <p>
                    A rule-based decision logic layer was developed to map user needs to product
                    features. This allowed the system to evaluate user intent, rank suitable options,
                    and generate recommendations with supporting explanations.
                </p>
            </div>
            """,
            unsafe_allow_html=True
        )

    st.markdown('<hr class="soft-divider">', unsafe_allow_html=True)

    process_cols_2 = st.columns(3, gap="medium")

    with process_cols_2[0]:
        st.markdown(
            """
            <div class="mini-card">
                <h3>4. System Integration</h3>
                <p>
                    The datasets were integrated into an AnythingLLM workspace, while the GPT model
                    was connected through OpenRouter. Retrieval-Augmented Generation was used to
                    improve contextual accuracy by retrieving relevant dataset information first.
                </p>
            </div>
            """,
            unsafe_allow_html=True
        )

    with process_cols_2[1]:
        st.markdown(
            """
            <div class="mini-card">
                <h3>5. Interface Development</h3>
                <p>
                    A Streamlit-based web interface was developed to make the system accessible and
                    easy to use. The interface supports informational queries, recommendations,
                    and comparisons in a clean and structured format.
                </p>
            </div>
            """,
            unsafe_allow_html=True
        )

    with process_cols_2[2]:
        st.markdown(
            """
            <div class="mini-card">
                <h3>6. Testing and Refinement</h3>
                <p>
                    The system was tested using sample users and different query types to assess
                    accuracy, relevance, and usability. Based on the findings, datasets, prompts,
                    and system settings were refined for better consistency and clarity.
                </p>
            </div>
            """,
            unsafe_allow_html=True
        )

    st.markdown(
        """
        <div class="soft-card">
            <h3>Major Challenges and Solutions</h3>
            <p>
                Several technical and functional challenges emerged during development.
                These issues were addressed through structured design decisions, testing,
                and continuous refinement.
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )

    challenge_cols_1 = st.columns(2, gap="medium")

    with challenge_cols_1[0]:
        with st.expander("Challenge: Data Inconsistency", expanded=False):
            st.markdown(
                """
                **Solution:**  
                Financial data from different banks varied in terminology, formatting,
                and level of detail. This was addressed by cleaning, standardizing,
                and reorganizing the data into a unified structure supported by predefined tags
                and consistent dataset formatting.
                """
            )

    with challenge_cols_1[1]:
        with st.expander("Challenge: User Intent Interpretation", expanded=False):
            st.markdown(
                """
                **Solution:**  
                The system handled clear queries well, but vague or indirect inputs were harder
                to interpret. A decision logic framework was introduced to map user inputs to
                predefined tags and improve response relevance through structured matching.
                """
            )

    st.markdown('<hr class="soft-divider">', unsafe_allow_html=True)

    challenge_cols_2 = st.columns(2, gap="medium")

    with challenge_cols_2[0]:
        with st.expander("Challenge: Response Quality and Performance", expanded=False):
            st.markdown(
                """
                **Solution:**  
                Early outputs were sometimes inconsistent or too long. This was improved by
                refining model configurations and optimizing the system prompt to produce
                clearer, shorter, and more structured responses for users.
                """
            )

    with challenge_cols_2[1]:
        with st.expander("Challenge: Security and Reliability", expanded=False):
            st.markdown(
                """
                **Solution:**  
                Prompt injection and attempts to access restricted information were considered
                during testing. System-level constraints were added to keep responses limited
                to dataset-driven content and preserve safe, intended behavior.
                """
            )

    show_site_tail()