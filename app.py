"""
Developer's Name: Khalia Phillips
App Name: FinFit JA
Version: 1.0
Purpose (File): This file manages the shared layout, styling, navigation, and page routing for the FinFit JA Streamlit app.
"""

import streamlit as st
from pathlib import Path

st.set_page_config(page_title="FinFit JA", page_icon="💵", layout="wide", initial_sidebar_state="expanded")

#Brand Values
AppTitle = "FinFit JA"
BuildTag = "v1.0"
MakerLine = "Created by Khalia Phillips"
RepoLink = "https://github.com/KPhil-cmatrix/finfitja.git"
ShortNote = "Academic prototype only. Please confirm final banking details directly with the institution."
FullNote = (
    "Disclaimer: FinFit JA is an academic prototype that uses the system's dataset to "
    "offer general banking recommendations and information. It does not claim to offer "
    "financial advice. Before arriving at any and all decisions, users should immediately "
    "verify all product details with the selected financial institution(s)."
)
RightsLine = "© 2026 Khalia Phillips. All rights reserved."
MarkPath = "FinFitLogo.png"

#Keeps track of the page currently being viewed
if "current_view" not in st.session_state:
        st.session_state.current_view = "Home"

#Adds the main site styling
def pour_style():
    st.markdown(
        """
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@600;700;800&family=Poppins:wght@400;500;600&display=swap');
        :root {
            --mint-main: #b6dfa1;
            --mint-soft: #edf7e7;
            --mint-cream: #f1f8ea;
            --base-bg: #fffdf7;
            --base-side: #f7f7eb;
            --line-soft: #d8d1b2;
            --ink-main: #111111;
            --ink-soft: #3b3b3b;
        }
        html, body, [class*="css"] {
            font-family: 'Poppins', sans-serif;
        }
        .stApp {
            background-color: var(--base-bg);
            color: var(--ink-main);
        }
        h1, h2, h3, h4, h5, h6 {
            font-family: 'Inter', sans-serif;
            color: var(--ink-main);
        }
        p, li {
            font-size: 1rem;
            font-weight: 500;
            color: var(--ink-main);
            line-height: 1.75;
        }
        section[data-testid="stSidebar"] {
            background: var(--base-side);
            border-right: 1px solid var(--line-soft);
        }
        section[data-testid="stSidebar"] .block-container {
            padding-top: 1rem;
            padding-bottom: 1rem;
        }
        .crest-wrap {
            text-align: center;
            margin-bottom: 1rem;
        }
        .crest-name {
            font-family: 'Inter', sans-serif;
            font-size: 1.3rem;
            font-weight: 800;
            color: var(--ink-main);
            margin-top: 0.35rem;
            margin-bottom: 0.1rem;
        }
        .crest-note {
            font-size: 0.92rem;
            color: var(--ink-soft);
            margin-bottom: 0.4rem;
        }
        .trail-label {
            font-size: 0.8rem;
            color: #5a5a5a;
            margin: 0.2rem 0 0.55rem 0.1rem;
        }
        .page-banner {
            background: linear-gradient(90deg, rgba(182,223,161,0.28) 0%, rgba(247,243,217,0.88) 100%);
            border: 1px solid var(--line-soft);
            border-radius: 18px;
            padding: 1.05rem 1rem 0.95rem 1rem;
            margin-bottom: 1rem;
            text-align: center;
        }
        .page-banner .title {
            font-family: 'Inter', sans-serif;
            font-size: 2.05rem;
            font-weight: 800;
            color: var(--ink-main);
            margin-bottom: 0.12rem;
        }
        .page-banner .subtitle {
            font-size: 1rem;
            font-weight: 600;
            color: #2f2f2f;
        }
        .panel-card {
            background: var(--mint-cream);
            border: 1px solid var(--line-soft);
            border-radius: 18px;
            padding: 1rem;
            margin-bottom: 1rem;
        }
        .panel-card h3 {
            margin-top: 0;
            margin-bottom: 0.7rem;
        }
        .site-tail {
            margin-top: 1.7rem;
            padding-top: 0.9rem;
            border-top: 1px solid var(--line-soft);
            text-align: center;
            font-size: 0.86rem;
            color: var(--ink-soft);
        }
        .side-tail {
            margin-top: 1rem;
            padding-top: 0.85rem;
            border-top: 1px solid rgba(0,0,0,0.12);
            text-align: center;
            font-size: 0.84rem;
            color: var(--ink-soft);
        }
        div.stButton > button {
            width: 100%;
            text-align: left;
            border-radius: 12px;
            border: 1px solid var(--line-soft);
            background: #ffffff;
            color: var(--ink-main);
            font-weight: 600;
            padding: 0.75rem 0.85rem;
            box-shadow: none;
        }
        div.stButton > button:hover {
            border-color: #9ecc85;
            color: var(--ink-main);
        }
        div.stButton > button:focus {
            box-shadow: none;
        }
                .hero-card {
            background: linear-gradient(135deg, rgba(182,223,161,0.24) 0%, rgba(247,243,217,0.82) 100%);
            border: 1px solid var(--line-soft);
            border-radius: 20px;
            padding: 1.2rem 1.1rem;
            margin-bottom: 1rem;
        }
        .hero-title {
            font-family: 'Inter', sans-serif;
            font-size: 2rem;
            font-weight: 800;
            color: var(--ink-main);
            margin-bottom: 0.35rem;
            text-align: center;
        }
        .mini-card {
            background: #ffffff;
            border: 1px solid var(--line-soft);
            border-radius: 18px;
            padding: 1rem;
            min-height: 210px;
        }
        .mini-card h3 {
            margin-top: 0;
            margin-bottom: 0.55rem;
            text-align: center;
        }
        .mini-card p {
            margin-bottom: 0;
        }
        .soft-card {
            background: var(--mint-cream);
            border: 1px solid var(--line-soft);
            border-radius: 18px;
            padding: 1rem;
            margin-bottom: 1rem;
        }
        .soft-card h3 {
            margin-top: 0;
            margin-bottom: 0.6rem;
        }
        .soft-card p, .soft-card li {
            margin-bottom: 0;
        }
        .guide-card {
            background: #ffffff;
            border: 1px solid var(--line-soft);
            border-radius: 16px;
            padding: 0.95rem;
            height: 100%;
        }
        .guide-card h4 {
            margin-top: 0;
            margin-bottom: 0.45rem;
            font-size: 1rem;
        }
        .guide-card p {
            margin-bottom: 0;
        }
        .note-box {
            background: #fffdf6;
            border: 1px solid var(--line-soft);
            border-left: 4px solid #a8cf8f;
            border-radius: 14px;
            padding: 0.9rem 1rem;
            margin-top: 0.2rem;
        }
        .note-box p {
            margin: 0;
        }
        .soft-divider {
            border: none;
            border-top: 1px solid var(--line-soft);
            margin: 1.25rem 0 1rem 0;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

#Shows the logo and app identity at the top of the sidebar
def show_crest():
    crest = Path(MarkPath)
    with st.sidebar:
        st.markdown('<div class="crest-wrap">', unsafe_allow_html=True)
        if crest.exists():
            left, mid, right = st.columns([1, 2, 1])
            with mid:
                st.image(str(crest), use_container_width=True)
        else:
            st.warning("Logo file not found. Please add it to the app folder.")
        st.markdown(f'<div class="crest-name">{AppTitle}</div>', unsafe_allow_html=True)
        st.markdown('<div class="crest-note">Jamaican Banking Recommendation Assistant</div>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

#Shows the sidebar navigation and keeps one tab active
def show_trail():
    st.sidebar.markdown('<div class="trail-label">Navigation</div>', unsafe_allow_html=True)
    pages = [
        "Home",
        "Ask FinFit",
        "Recommendation Generator",
        "Comparison Profile",
        "Dev Process",
        "Performance Metrics"
    ]
    for page in pages:
        clicked = st.sidebar.button(page, key=f"nav_{page}", use_container_width=True)
        if clicked:
            st.session_state.current_view = page

#Shows the active page in a clean banner at the top
def show_banner(page_name: str):
    st.markdown(
        f"""
        <div class="page-banner">
            <div class="title">{AppTitle}</div>
            <div class="subtitle">{page_name}</div>
        </div>
        """,
        unsafe_allow_html=True
    )

#Shows the site footer
def show_site_tail():
    st.markdown(
        f"""
        <div class="site-tail">
            <div style="margin-bottom:0.35rem;"><strong>{ShortNote}</strong></div>
            <div>{RightsLine}</div>
        </div>
        """,
        unsafe_allow_html=True
    )

#Shows the lower sidebar information
def show_trail_end():
    st.sidebar.markdown(
        f"""
        <div class="side-tail">
            <div><strong>{BuildTag}</strong></div>
            <div>{MakerLine}</div>
            <div style="margin-top:0.4rem;"><a href="{RepoLink}" target="_blank">GitHub</a></div>
        </div>
        """,
        unsafe_allow_html=True
    )

#Temporary page block until each section is built
def hold_page(title: str, text: str):
    show_banner(title)
    st.markdown(
        f"""
        <div class="panel-card">
            <h3>Coming Next</h3>
            <p style="margin-bottom:0;">{text}</p>
        </div>
        """,
        unsafe_allow_html=True
    )
    show_site_tail()

#Landing/Home Page
def open_landing():
    show_banner("Home")
    col1, col2 = st.columns([1.15, 1.85], gap="medium")
    with col1:
        crest = Path(MarkPath)
        if crest.exists():
            left, mid, right = st.columns([1, 2, 1])
            with mid:
                st.image(str(crest), use_container_width=True)
        st.markdown('<div class="hero-title">Smarter Banking Starts Here.</div>', unsafe_allow_html=True)
    with col2:
        st.markdown(
            """
            <div class="soft-card">
                <h3>What is FinFit JA?</h3>
                <p>FinFit JA is a custom GPT-powered assistant created for the Jamaican banking sector. 
                It was designed to make it simpler for customers to compare financial products across financial institutions, 
                understand the banking product options that exist, and receive more pertinent advice without having to sift through dispersed information on their own, 
                through a bank's biased lens.</p>
            </div>
            """,
            unsafe_allow_html=True
        )
        st.markdown(
            """
            <div class="note-box">
                <p><strong>Whether someone is a student, a first-time account holder, or an established working professional, 
                FinFit JA is meant to support clearer and more confident banking decisions.</strong></p>
            </div>
            """,
            unsafe_allow_html=True
        )
    st.markdown('<div style="height:0.75rem;"></div>', unsafe_allow_html=True)   
    st.markdown(
        """
        <div class="soft-card">
            <h3>Why This Matters</h3>
            <p>Selecting financial services on your own can be difficult, particularly when products from different banks seem similar at first glance 
            but differ in terms of fees, access, digital features, opening criteria, and general fit. 
            FinFit JA was created to assist users in overcoming this complexity by transforming banking data into more practical, user-focused guidance.</p>
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
                <p>Depending on their requirements, such as low fees, student-friendly access, or mobile banking preferences, users can receive personalized account recommendations.</p>
            </div>
            """,
            unsafe_allow_html=True
        )
    with aid2:
        st.markdown(
            """
            <div class="mini-card">
                <h3>Structured              <br>Comparisons</h3>
                <p>FinFit JA can make it easier to recognize differences in features, convenience, and suitability by comparing banks and accounts in a streamlined and logical manner.</p>
            </div>
            """,
            unsafe_allow_html=True
        )
    with aid3:
        st.markdown(
            """
            <div class="mini-card">
                <h3>Actionable<br>            Guidance</h3>
                <p>By providing answers in a more approachable and useful format, the system also aims to make financial decisions seem less daunting to the wider Jamaican public.</p>
            </div>
            """,
            unsafe_allow_html=True
        )
    st.markdown('<hr class="soft-divider">', unsafe_allow_html=True)
    st.markdown(
        """
        <div class="soft-card">
            <h3>How to Navigate the Platform</h3>
            <p>Each distinct aspect of the FinFit JA experience is supported by a different part of the app. Depending on what you want to do, you can move between them using the sidebar.</p>
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
                <p>Use this when you want to ask general banking questions in a natural chat format.</p>
            </div>
            """,
            unsafe_allow_html=True
        )
        st.markdown(
            """
            <div class="guide-card">
                <h4>Recommendation Generator</h4>
                <p>Use this when you want the system to recommend accounts based on structured preferences and banking needs.</p>
            </div>
            """,
            unsafe_allow_html=True
        )
        st.markdown(
            """
            <div class="guide-card">
                <h4>Comparison Profile</h4>
                <p>Use this when you want to compare banks or account options side by side in a more focused way.</p>
            </div>
            """,
            unsafe_allow_html=True
        )
    with use2:
        st.markdown(
            """
            <div class="guide-card">
                <h4>Dev Process</h4>
                <p>Use this section to learn how the system was developed, including technical choices, design decisions, and implementation challenges.</p>
            </div>
            """,
            unsafe_allow_html=True
        )
        st.markdown(
            """
            <div class="guide-card">
                <h4>Performance Metrics</h4>
                <p>Use this section to review the testing approach, evaluation process, and the overall performance of the custom GPT.</p>
            </div>
            """,
            unsafe_allow_html=True
        )
        st.markdown(
            """
            <div class="guide-card">
                <h4>Home</h4>
                <p>You are here. This page introduces the purpose of FinFit JA and shows how to navigate the site effectively.</p>
            </div>
            """,
            unsafe_allow_html=True
        )
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
    
#Ask FinFit Chat
def open_chat():
    hold_page("Ask FinFit", "This page will contain the standard chat interface and a clear chat control.")

#Recommendation Generator
def open_matcher():
    hold_page("Recommendation Generator", "This page will contain structured banking inputs with recommendation results beside them.")

#Comparison Profile
def open_compare():
    hold_page("Comparison Profile", "This page will contain tools for comparing banks and account types.")

#Dev Process
def open_build():
    hold_page("Dev Process", "This page will outline the development process, major challenges, and the solutions used.")

#Performance Metrics
def open_scores():
    hold_page("Performance Metrics", "This page will show testing results, performance metrics, and evaluation notes.")

#Routes the user to the correct page
def route_view(page_name: str):
    views = {
        "Home": open_landing,
        "Ask FinFit": open_chat,
        "Recommendation Generator": open_matcher,
        "Comparison Profile": open_compare,
        "Dev Process": open_build,
        "Performance Metrics": open_scores
    }
    views.get(page_name, open_landing)()

#Runs the shared layout
def main():
    pour_style()
    show_crest()
    show_trail()
    show_trail_end()
    route_view(st.session_state.current_view)

if __name__ == "__main__":
    main()
