"""
Developer's Name: Khalia Phillips
App Name: FinFit JA
Version: 1.0
Purpose (File): This file manages the Performance Metrics page for the FinFit JA Streamlit app.
"""

import pandas as pd
import streamlit as st
from layout import show_banner, show_site_tail


#Performance Metrics Page
def open_scores():
    show_banner("Performance Metrics")

    st.markdown(
        """
        <div class="soft-card">
            <h3>Pilot Testing Results and Evaluation Summary</h3>
            <p>
                FinFit JA was evaluated through structured pilot testing to assess its effectiveness,
                reliability, and overall user experience. Testing involved six participants from varied
                backgrounds, each completing two queries, resulting in twelve total interactions across
                recommendation, comparison, informational, and adversarial query types.
                <br><br>
                Performance was measured using four key indicators: accuracy, relevance, user satisfaction,
                and response appropriateness, each scored on a scale of 1 to 5.
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )

    metric_table = pd.DataFrame(
        [
            {
                "Metric": "Accuracy",
                "Average Score": 4.9,
                "Interpretation": "Strong retrieval, interpretation, and correct use of dataset-driven information."
            },
            {
                "Metric": "Relevance",
                "Average Score": 4.4,
                "Interpretation": "Strong overall, with minor limitations when queries were vague or indirectly phrased."
            },
            {
                "Metric": "User Satisfaction",
                "Average Score": 4.8,
                "Interpretation": "Users found the system intuitive, useful, and aligned with their expectations."
            },
            {
                "Metric": "Response Appropriateness",
                "Average Score": 4.5,
                "Interpretation": "Responses remained structured, suitable, and functionally consistent within scope."
            }
        ]
    )

    st.markdown(
        """
        <div class="soft-card">
            <h3>Performance Overview</h3>
            <p>
                The table below summarizes the system’s average scores across the four evaluation metrics.
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.table(metric_table)

    st.markdown('<hr class="soft-divider">', unsafe_allow_html=True)

    insight_cols = st.columns(3, gap="medium")

    with insight_cols[0]:
        with st.expander("What Worked Well", expanded=False):
            st.markdown(
                """
                FinFit JA consistently generated accurate and well-structured responses grounded in its
                datasets. It maintained standardized outputs, referenced specific account information,
                and avoided relying on generic or assumed recommendations.
                """
            )

    with insight_cols[1]:
        with st.expander("Limitations Identified", expanded=False):
            st.markdown(
                """
                A limitation was observed when handling ambiguous or subtly negative queries.
                In some cases, the system attempted to respond directly instead of requesting clarification,
                indicating that intent recognition and clarification handling could be improved further.
                """
            )

    with insight_cols[2]:
        with st.expander("Security and Reliability", expanded=False):
            st.markdown(
                """
                The system demonstrated effective resistance to prompt injection and unauthorized
                data access attempts. It refused to disclose sensitive information while continuing
                to respond appropriately to legitimate parts of user queries.
                """
            )

    st.markdown('<hr class="soft-divider">', unsafe_allow_html=True)

    bottom_cols = st.columns(2, gap="medium")

    with bottom_cols[0]:
        with st.expander("Response Efficiency", expanded=False):
            st.markdown(
                """
                Minor delays in response time were observed during testing. However, users generally
                considered this acceptable given the system’s high accuracy, structured responses,
                and clear recommendations.
                """
            )

    with bottom_cols[1]:
        with st.expander("Overall Conclusion", expanded=False):
            st.markdown(
                """
                Overall, the findings indicate that FinFit JA is a reliable and effective decision-support
                tool for banking guidance in Jamaica. The results also highlight opportunities for
                improvement in query interpretation, clarification handling, and response efficiency
                as the system continues to evolve.
                """
            )

    show_site_tail()