"""
Developer's Name: Khalia Phillips
App Name: FinFit JA
Version: 1.0
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
                including the main implementation stages, workflow structure, and key improvements
                made throughout the project.
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown('<div class="section-title">How FinFit JA Was Built</div>', unsafe_allow_html=True)
    st.markdown('<hr class="soft-divider">', unsafe_allow_html=True)

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
                    was connected through OpenRouter. Retrieval-Augmented Generation (RAG) was used
                    to improve contextual accuracy by retrieving relevant dataset information before
                    generating responses.
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
                    easy to use. The interface was designed to support natural interaction through
                    informational queries, recommendations, and comparisons in a clean, structured format.
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
                    accuracy, relevance, and usability. Based on the findings, datasets were refined,
                    response structure was improved, and system configurations were adjusted for
                    better consistency and clarity.
                </p>
            </div>
            """,
            unsafe_allow_html=True
        )

    st.markdown('<div class="section-title">How the System Responds</div>', unsafe_allow_html=True)
    st.markdown('<hr class="soft-divider">', unsafe_allow_html=True)

    workflow_cols = st.columns(3, gap="medium")

    with workflow_cols[0]:
        st.markdown(
            """
            <div class="guide-card">
                <h4>Input and Detection</h4>
                <p>
                    The user provides non-sensitive personal and financial preferences, and the system
                    identifies key needs, intent, and relevant priorities from the input.
                </p>
            </div>
            """,
            unsafe_allow_html=True
        )

    with workflow_cols[1]:
        st.markdown(
            """
            <div class="guide-card">
                <h4>Matching and Ranking</h4>
                <p>
                    Detected needs are mapped to account features and matched against available banking
                    products. Suitable options are then ranked based on rule-based scoring.
                </p>
            </div>
            """,
            unsafe_allow_html=True
        )

    with workflow_cols[2]:
        st.markdown(
            """
            <div class="guide-card">
                <h4>Output Generation</h4>
                <p>
                    The system produces one main recommendation along with alternatives and short
                    explanations, helping users make more informed banking decisions.
                </p>
            </div>
            """,
            unsafe_allow_html=True
        )

    st.markdown('<div class="section-title">Major Challenges and Solutions</div>', unsafe_allow_html=True)
    st.markdown('<hr class="soft-divider">', unsafe_allow_html=True)

    challenge_cols_1 = st.columns(2, gap="medium")

    with challenge_cols_1[0]:
        st.markdown(
            """
            <div class="soft-card">
                <h3>Data Inconsistency</h3>
                <p>
                    Financial data from different banks varied in formatting, terminology, and level
                    of detail. This was addressed by cleaning, standardizing, and reorganizing the
                    data into a unified structure supported by predefined tags and formats.
                </p>
            </div>
            """,
            unsafe_allow_html=True
        )

    with challenge_cols_1[1]:
        st.markdown(
            """
            <div class="soft-card">
                <h3>User Intent Interpretation</h3>
                <p>
                    The system handled clear queries well, but vague or indirect inputs were more
                    difficult to interpret. A decision logic framework was introduced to map user
                    inputs to predefined tags and improve response relevance.
                </p>
            </div>
            """,
            unsafe_allow_html=True
        )

    challenge_cols_2 = st.columns(2, gap="medium")

    with challenge_cols_2[0]:
        st.markdown(
            """
            <div class="soft-card">
                <h3>Response Quality and Performance</h3>
                <p>
                    Early outputs were sometimes inconsistent or too long. This was improved by
                    refining model configurations and optimizing the system prompt to produce
                    clearer, shorter, and more structured responses.
                </p>
            </div>
            """,
            unsafe_allow_html=True
        )

    with challenge_cols_2[1]:
        st.markdown(
            """
            <div class="soft-card">
                <h3>Security and Reliability</h3>
                <p>
                    Prompt injection and attempts to access restricted information were considered
                    during testing. System-level constraints were added to keep responses limited
                    to dataset-driven content and preserve safe, intended behavior.
                </p>
            </div>
            """,
            unsafe_allow_html=True
        )

    show_site_tail()
