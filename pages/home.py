"""
Developer: Khalia Phillips
App: FinFit JA
Version: 1.5
Purpose: Manages the Home page.
"""

from pathlib import Path
import streamlit as st
from layout import FullNote, MainMarkPath, show_banner, show_site_tail

#Opening the Home page
def open_landing():
    show_banner("Home")
    col1, col2 = st.columns([1.15, 1.85], gap="medium")
    with col1:
        logo = Path(MainMarkPath)
        if logo.exists():
            left, center, right = st.columns([1, 2, 1])
            with center:
                st.image(str(logo), width=240)
        st.markdown('<div class="hero-title">Smarter Banking Starts Here.</div>', unsafe_allow_html=True)
    with col2:
        st.markdown(
            """
            <div class="soft-card">
                <h3>What is FinFit JA?</h3>
                <p>FinFit JA is a custom GPT-powered assistant created for the Jamaican banking sector. 
                It was designed to make it easier for customers to compare similar products across financial institutions, 
                better understand the options available to them, and receive relevant guidance without having to sort through scattered information on their own.</p>
            </div>
            """,
            unsafe_allow_html=True
        )
        st.markdown(
            """
            <div class="note-box">
                <p><strong>"From students who are just starting out, to established working professionals who are looking to optimize their financial portfolios, 
                FinFit JA is designed to help everyone find their best financial fit." - Khalia Phillips, 2026</strong></p>
            </div>
            """,
            unsafe_allow_html=True
        )
    st.markdown('<div style="height:0.75rem;"></div>', unsafe_allow_html=True)
    st.markdown(
        """
        <div class="soft-card">
            <h3>Why This Matters in Jamaican Banking</h3>
            <p>The process of selecting financial services on your own can be both challenging and time-consuming, 
            especially when products from different banks seem similar at first glance but differ greatly in accessibility, 
            digital features, and general suitability. 
            Information is frequently scattered across multiple sources in the Jamaican banking sector, 
            making it harder for customers to make well-informed decisions.</p>
            <br>
            <p>FinFit JA is designed to address these issues by providing a user-friendly interface that consolidates information and offers more personalized guidance, 
            making it easier for users to navigate the banking landscape and make decisions that better align with their financial goals and needs.</p>
        </div>
        """,
        unsafe_allow_html=True
    )
    aid1, aid2, aid3 = st.columns(3, gap="medium")
    with aid1:
        st.markdown(
            """
            <div class="mini-card">
                <h3>Tailored Recommendations</h3>
                <p>Depending on their needs, such as low fees, student-friendly access, 
                or mobile banking preferences, users can receive more personalized account recommendations.</p>
            </div>
            """,
            unsafe_allow_html=True
        )
    with aid2:
        st.markdown(
            """
            <div class="mini-card">
                <h3>Structured<br>Comparisons</h3>
                <p>FinFit JA makes it easier to identify differences in features, convenience, 
                and suitability by comparing banks and accounts in a streamlined and logical way.</p>
            </div>
            """,
            unsafe_allow_html=True
        )
    with aid3:
        st.markdown(
            """
            <div class="mini-card">
                <h3>Actionable<br>Guidance</h3>
                <p>By presenting responses in a more approachable format, 
                the system also aims to make financial decision-making feel less daunting to the wider Jamaican public.</p>
            </div>
            """,
            unsafe_allow_html=True
        )
    st.markdown('<hr class="soft-divider">', unsafe_allow_html=True)
    st.markdown(
        """
        <div class="soft-card">
            <h3>How to Navigate the Platform</h3>
            <p>Each distinct aspect of the FinFit JA experience is supported by a different component of the app. 
            Depending on your goal, you can move between them using the sidebar.</p>
        </div>
        """,
        unsafe_allow_html=True
    )
    use1, use2 = st.columns(2, gap="medium")
    with use1:
        st.markdown(
            """
            <div class="guide-card">
                <h4>Ask FinFit</h4>
                <p>Get instant answers to your banking questions in a simple, chat-based format.</p>
            </div>
            """,
            unsafe_allow_html=True
        )
        st.markdown(
            """
            <div class="guide-card">
                <h4>Recommendation Generator</h4>
                <p>Find bank accounts tailored to your needs based on your preferences and financial goals.</p>
            </div>
            """,
            unsafe_allow_html=True
        )
        st.markdown(
            """
            <div class="guide-card">
                <h4>Comparison Profile</h4>
                <p><p>Compare banks or accounts side by side to clearly see differences in features, accessibility, and overall fit.</p>
            </div>
            """,
            unsafe_allow_html=True
        )
    with use2:
        st.markdown(
            """
            <div class="guide-card">
                <h4>Development Overview</h4>
                <p>A behind-the-scenes look at how FinFit JA was designed, built, tested, and refined.</p>
            </div>
            """,
            unsafe_allow_html=True
        )
        st.markdown(
            """
            <div class="guide-card">
                <h4>Performance Metrics</h4>
                <p>A detailed overview of system performance metrics and evaluation insights.</p>
            </div>
            """,
            unsafe_allow_html=True
        )
        st.markdown(
            """
            <div class="guide-card">
                <h4>Home</h4>
                <p>Where you are. Start here for a quick introduction to FinFit JA and a guide to navigating its features.</p>
            </div>
            """,
            unsafe_allow_html=True
        )
    st.markdown('<hr class="soft-divider">', unsafe_allow_html=True)
    st.markdown('<div style="height:0.75rem;"></div>', unsafe_allow_html=True)
    st.markdown(
        f"""
        <div class="soft-card">
            <h3>Full Disclaimer</h3>
            <p>{FullNote}</p>
        </div>
        """,
        unsafe_allow_html=True
    )
    show_site_tail()