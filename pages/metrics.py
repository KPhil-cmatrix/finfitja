"""
Developer: Khalia Phillips
App: FinFit JA
Version: 1.4
Purpose: Manages the Performance Metrics page.
"""

import pandas as pd
import streamlit as st
from layout import show_banner, show_site_tail

#Defining the Performance Metrics page
def open_scores():
    show_banner("Performance Metrics")
    st.markdown(
        """
        <div class="soft-card">
            <h3>Performance Overview</h3>
            <p>FinFit JA was evaluated through a structured pilot testing process involving fifteen users from varied backgrounds, each completing three queries. 
            This resulted in forty-five total interactions across recommendation, comparison, informational, and adversarial query types, 
            allowing the system to be assessed across a broader range of user needs and interaction styles.</p>
            <br>
            <p>The table below summarizes the system's average scores across four evaluation indicators, each measured on a ten-point scale. 
            The expandable sections that follow provide a more practical interpretation of what performed well, where limitations were observed, 
            and what the results suggest about the system's overall reliability and readiness.</p>
        </div>
        """,
        unsafe_allow_html=True
    )
    metric_table = pd.DataFrame(
        [
            {
                "Metric": "Accuracy",
                "Average Score (/10)": 9.3,
                "Interpretation": "Strong retrieval, interpretation, and correct use of dataset-driven information."
            },
            {
                "Metric": "Relevance",
                "Average Score (/10)": 8.8,
                "Interpretation": "Strong overall, with minor limitations when queries were vague or indirectly phrased."
            },
            {
                "Metric": "User Satisfaction",
                "Average Score (/10)": 9.1,
                "Interpretation": "Users found the system intuitive, useful, and aligned with their expectations."
            },
            {
                "Metric": "Response Appropriateness",
                "Average Score (/10)": 8.9,
                "Interpretation": "Responses remained structured, suitable, and functionally consistent within scope."
            }
        ]
    )
    table_rows = ""
    for _, row in metric_table.iterrows():
        table_rows += f"""
        <tr>
            <td>{row["Metric"]}</td>
            <td>{row["Average Score (/10)"]:.1f}</td>
            <td>{row["Interpretation"]}</td>
        </tr>
        """
    st.markdown(
        f"""
        <div style="background:#ffffff; border:1px solid #d8d1b2; border-radius:16px; overflow:hidden; margin-bottom:1rem;">
            <div style="padding:1rem 1.2rem; border-bottom:1px solid #d8d1b2; font-weight:600; font-size:1.05rem; background:#ffffff;">
                Evaluation Metrics Summary
            </div>
            <table style="width:100%; border-collapse:collapse; background:#ffffff;">
                <thead>
                    <tr>
                        <th style="text-align:left; padding:0.9rem 1rem; border-bottom:1px solid #d8d1b2;">Metric</th>
                        <th style="text-align:left; padding:0.9rem 1rem; border-bottom:1px solid #d8d1b2;">Average Score (/10)</th>
                        <th style="text-align:left; padding:0.9rem 1rem; border-bottom:1px solid #d8d1b2;">Interpretation</th>
                    </tr>
                </thead>
                <tbody>
                    {table_rows}
                </tbody>
            </table>
        </div>
        <style>
        table tbody tr td {{
            padding: 0.9rem 1rem;
            border-bottom: 1px solid #d8d1b2;
            vertical-align: top;
            background:#ffffff;
        }}
        table tbody tr:last-child td {{
            border-bottom: none;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )
    insight_cols = st.columns(3, gap="medium")
    with insight_cols[0]:
        with st.expander("What Worked Well", expanded=False):
            st.markdown(
                """
                FinFit JA consistently generated accurate and well-structured responses grounded in its datasets. 
                It avoided depending on general or presumptive recommendations, maintained standardized outputs, and cited particular account information.
                Since responses followed a standard format that contained both explanations and other alternative options, users were able to easily understand why specific accounts or banks were suggested.  
                This, in turn, contributed to a more transparent and trustworthy user experience.
                Additionally, Strong alignment between user inputs and output recommendations was also demonstrated by the system, suggesting that the rule-based decision logic and tagging algorithm were operating efficiently across various query types.
                """
            )
    with insight_cols[1]:
        with st.expander("Limitations Identified", expanded=False):
            st.markdown(
                """
                A limitation was observed when handling ambiguous or subtly negative queries. 
                In certain instances, the system tried to answer directly rather than ask for clarification, suggesting that intent detection and handling of clarification may be further enhanced.
                This was particularly evident in questions where the user's choices were not fully expressed or were expressed in an indirect manner, which sometimes resulted in somewhat accurate but poorly personalized answers.  
                It can be deducted then, that enhancing the system's ability to identify ambiguity and request clarification would improve overall accuracy.
                Furthermore, there were a few discrepancies in the interpretation of edge-case requests, indicating that the decision logic and prompt structure may be further improved to provide a greater robustness in less straightforward cases.
                """
            )
    with insight_cols[2]:
        with st.expander("Security and Reliability", expanded=False):
            st.markdown(
                """
                The system demonstrated effective resistance to prompt injection and unauthorized data access attempts. 
                It continued to appropriately respond to valid portions of user inquiries while refusing to reveal sensitive information.
                During adversarial testing, the model maintained its structured response behavior and did not deviate from its dataset-driven constraints, reinforcing its reliability as a controlled decision-support tool.
                This demonstrates that the system's prompt design and dataset restrictions successfully enforced boundaries, ensuring that outputs were secure, relevant, and within the intended application scope.
                """
            )
    bottom_cols = st.columns(2, gap="medium")
    with bottom_cols[0]:
        with st.expander("Response Efficiency", expanded=False):
            st.markdown(
                """
                There were slight delays in response time that were observed during testing, particularly when handling more complex recommendation or comparison queries. 
                These delays were primarily influenced by the system’s reliance on an external API (OpenRouter), where response times can vary due to factors outside of direct system control.
                However, considering the system's high accuracy, well-organized responses, and well-tailored recommendations, users generally regarded this as acceptable. 
                With further optimization of model configuration and backend processing, response times could be improved without compromising the quality and reliability of the system's outputs.
                """
            )
    with bottom_cols[1]:
        with st.expander("Overall Conclusion", expanded=False):
            st.markdown(
                """
                In summary, the findings indicate that FinFit JA is a reliable and effecient decision-support tool for banking assistance in Jamaica. 
                The system scored very well under all evaluation metrics, particularly in terms of its accuracy and user satisfaction level.
                Its ability to generate structured, dataset-driven recommendations positions it as a practical solution for simplifying financial decision-making, especially for users who may find traditional banking information overwhelming.
                While there are opportunities for improvement in query interpretation, clarification handling, and response efficiency, the current implementation provides a strong foundation for further development and real-world application.
                """
            )
    show_site_tail()