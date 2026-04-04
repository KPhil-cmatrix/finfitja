"""
Developer: Khalia Phillips
App: FinFit JA
Version: 1.9
Purpose: Manages the shared styling, sidebar layout, page banner, footer, and common platform elements for the FinFit JA Streamlit app.
"""

from pathlib import Path
import streamlit as st

#Brand Values
AppTitle = "FinFit JA"
BuildTag = "v1.0"
MakerLine = "Created by Khalia Phillips"
RepoLink = "https://github.com/KPhil-cmatrix/finfitja.git"
ShortNote = "Academic prototype only. Please confirm final banking details directly with the institution."
FullNote = (
    "Disclaimer: FinFit JA is an academic prototype that uses the system's dataset to "
    "offer general banking recommendations and information. It does not claim to offer "
    "financial advice. Before making any final decisions, users should immediately verify "
    "all product details with the selected financial institution(s)."
)
RightsLine = "© 2026 Khalia Phillips. All rights reserved."
SidebarMarkPath = "FinFitLogoSidebar.png"
MainMarkPath = "FinFitLogo.png"

#Adding the main site styling
def pour_style():
    st.markdown(
        """
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@600;700;800&family=Poppins:wght@400;500;600&display=swap');
        :root {
            --base-bg: #fffdf7;
            --base-side: #f7f7eb;
            --banner-fill: #f7f3d9;
            --ink-main: #111111;
            --ink-soft: #3b3b3b;
            --line-soft: #d8d1b2;
            --mint-cream: #f1f8ea;
            --mint-main: #b6dfa1;
            --mint-soft: #edf7e7;
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
        h1 {
            font-size: 2.2rem;
            font-weight: 800;
        }
        h2 {
            font-size: 1.65rem;
            font-weight: 700;
        }
        h3 {
            font-size: 1.3rem;
            font-weight: 700;
        }
        h4 {
            font-size: 1.1rem;
            font-weight: 600;
        }
        p, li {
            font-size: 1rem;
            font-weight: 400;
            color: var(--ink-main);
            line-height: 1.75;
        }
        section[data-testid="stSidebar"] {
           background-color: var(--banner-fill) !important;
        }
        section[data-testid="stSidebar"] div.stButton > button {
            width: 100%;
            min-height: 64px;
            text-align: center;
            border-radius: 18px;
            border: 1px solid var(--line-soft);
            background: #ffffff;
            color: var(--ink-main);
            font-weight: 600;
            font-size: 1.02rem;
            padding: 0.9rem 1rem;
            box-shadow: none;
            margin-bottom: 0.55rem;
            transition: all 0.18s ease;
        }
        section[data-testid="stSidebar"] div.stButton > button:hover {
            border-color: #9ecc85;
            background: #fcfff9;
        }
        section[data-testid="stSidebar"] div.stButton > button:focus {
            box-shadow: none;
            border-color: #9ecc85;
        }
        section[data-testid="stSidebar"] div.stButton > button:disabled {
            background: #fcfff9;
            color: var(--ink-main);
            border: 1px solid var(--line-soft);
            box-shadow: inset 6px 0 0 #9ecc85;
            font-weight: 800 !important;
            font-size: 1.16rem;
            opacity: 1;
            cursor: default;
            -webkit-text-fill-color: var(--ink-main) !important;
        }
        .crest-wrap {
            text-align: center;
            margin-bottom: 1.1rem;
        }
        .crest-image {
            width: 100%;
            display: flex;
            justify-content: center;
            margin-bottom: 0.7rem;
        }
        .crest-name {
            font-family: 'Inter', sans-serif;
            font-size: 1.95rem;
            font-weight: 800;
            color: var(--ink-main);
            margin: 0.15rem 0;
            text-align: left;
        }
        .crest-note {
            font-size: 1rem;
            color: var(--ink-soft);
            margin-bottom: 0.55rem;
            text-align: left;
            line-height: 1.55;
        }
        .trail-label {
            font-size: 0.92rem;
            font-weight: 600;
            color: #5a5a5a;
            margin: 0.4rem 0 0.7rem 0.1rem;
        }
        .page-banner {
            background: var(--banner-fill);
            border: 1px solid var(--line-soft);
            border-radius: 18px;
            padding: 1.05rem 1rem 0.95rem 1rem;
            margin-bottom: 1rem;
            text-align: center;
        }
        .page-banner .title {
            font-family: 'Inter', sans-serif;
            font-size: 2.3rem;
            font-weight: 800;
            color: var(--ink-main);
            margin-bottom: 0.18rem;
        }
        .page-banner .subtitle {
            font-size: 1.35rem;
            font-weight: 700;
            color: #2f2f2f;
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
        .mini-card {
            background: #ffffff;
            border: 1px solid var(--line-soft);
            border-radius: 18px;
            padding: 1rem;
            min-height: 230px;
        }
        .mini-card h3 {
            margin-top: 0;
            margin-bottom: 0.75rem;
            text-align: center;
            min-height: 88px;
            display: flex;
            align-items: center;
            justify-content: center;
        }
        .mini-card p {
            margin-bottom: 0;
            text-align: justify;
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
        }
        .guide-card p {
            margin-bottom: 0;
        }
        .result-card {
            background: #ffffff;
            border: 1px solid var(--line-soft);
            border-radius: 18px;
            padding: 1rem;
            min-height: 430px;
        }
        .result-card p:first-child,
        .result-card h1:first-child,
        .result-card h2:first-child,
        .result-card h3:first-child,
        .result-card h4:first-child {
            margin-top: 0;
        }
        .empty-result {
            display: flex;
            flex-direction: column;
            justify-content: center;
            color: var(--ink-soft);
        }
        .hero-title {
            font-family: 'Inter', sans-serif;
            font-size: 2rem;
            font-weight: 800;
            text-align: center;
            margin-bottom: 0.35rem;
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
        .chat-wrap {
            background: #ffffff;
            border: 1px solid var(--line-soft);
            border-radius: 18px;
            padding: 1rem;
            margin-bottom: 0.75rem;
        }
        .msg-user {
            background: #eef6e9;
            border: 1px solid var(--line-soft);
            border-radius: 14px;
            padding: 0.6rem 0.8rem;
            margin-bottom: 0.5rem;
        }
        .msg-bot {
            background: #ffffff;
            border: 1px solid var(--line-soft);
            border-radius: 14px;
            padding: 0.6rem 0.8rem;
            margin-bottom: 0.5rem;
        }
        .msg-label {
            font-size: 0.75rem;
            font-weight: 600;
            margin-bottom: 0.2rem;
            color: var(--ink-soft);
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
            box-shadow: none;
        }
        .match-panel {
            background: #ffffff;
            border: 1px solid var(--line-soft);
            border-radius: 18px;
            padding: 1rem;
            height: 560px;
            overflow-y: auto;
            box-sizing: border-box;
        }
        .match-panel h3 {
            text-align: center;
            margin-top: 0;
            margin-bottom: 0.75rem;
        }
        .match-panel p {
            margin-bottom: 0.8rem;
        }
        .result-panel {
            background: #ffffff;
            border: 1px solid var(--line-soft);
            border-radius: 18px;
            padding: 1rem;
            height: 560px;
            overflow-y: auto;
            box-sizing: border-box;
        }
        .result-panel h3 {
            text-align: center;
            margin-top: 0;
            margin-bottom: 0.75rem;
        }
        .section-title {
            font-family: 'Inter', sans-serif;
            font-size: 1.45rem;
            font-weight: 700;
            color: var(--ink-main);
            margin-bottom: 0.2rem;
        }
        details {
            border: 1px solid var(--line-soft);
            border-radius: 16px;
            background: #ffffff;
            padding: 0.2rem 0.4rem;
            margin-bottom: 0.8rem;
        }
        details summary {
            font-weight: 600;
            color: var(--ink-main);
            cursor: pointer;
        }
        details p {
            margin-bottom: 0.3rem;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

#Showing the logo and app identity at the top of the sidebar
def show_crest():
    crest = Path(SidebarMarkPath)
    with st.sidebar:
        st.markdown('<div class="crest-wrap">', unsafe_allow_html=True)
        st.markdown('<div class="crest-image">', unsafe_allow_html=True)
        if crest.exists():
            st.image(str(crest), use_container_width=True)
        else:
            st.warning("Sidebar logo file not found. Please add it to the app folder.")
        st.markdown('</div>', unsafe_allow_html=True)
        st.markdown(f'<div class="crest-name">{AppTitle}</div>', unsafe_allow_html=True)
        st.markdown('<div class="crest-note">Jamaican Banking Recommendation Assistant</div>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

#Showing the sidebar navigation and tracking the active page
def show_trail():
    st.sidebar.markdown('<div class="trail-label">Navigation</div>', unsafe_allow_html=True)
    pages = [
        "Home",
        "Ask FinFit",
        "Recommendation Generator",
        "Comparison Profile",
        "Development Overview",
        "Performance Metrics"
    ]
    for page in pages:
        is_active = st.session_state.current_view == page
        clicked = st.sidebar.button(
            page,
            key=f"nav_{page}",
            use_container_width=True,
            disabled=is_active
        )
        if clicked:
            st.session_state.current_view = page
            st.rerun()

#Showing the active page in the top banner
def show_banner(page_name:str):
    st.markdown(
        f"""
        <div class="page-banner">
            <div class="title">{AppTitle}</div>
            <div class="subtitle">{page_name}</div>
        </div>
        """,
        unsafe_allow_html=True
    )

#Showing the site footer
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

#Showing the lower sidebar information
def show_trail_end():
    st.sidebar.markdown(
        f"""
        <div class="side-tail">
            <div><strong>{BuildTag}</strong></div>
            <div>{MakerLine}</div>
            <div style="margin-top:0.4rem;"><a href="{RepoLink}" target="_blank">GitHub Repository</a></div>
        </div>
        """,
        unsafe_allow_html=True
    )
