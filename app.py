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
RepoLink = "https://github.com/your-username/your-repo"
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
    st.session_state.current_view = "Landing Page"

#Adds the main site styling
def pour_style():
    st.markdown(
        """
        <style>
        :root {
            --mint-main: #a8d98a;
            --mint-soft: #dff0d0;
            --cream-main: #fbf7e8;
            --cream-deep: #f6eec8;
            --line-soft: #d9d1ae;
            --ink-main: #111111;
            --card-wash: rgba(255, 248, 225, 0.75);
        }
        .stApp {
            background-color: var(--cream-main);
            color: var(--ink-main);
        }
        section[data-testid="stSidebar"] {
            background: linear-gradient(180deg, #eef7e6 0%, #f8f3d9 100%);
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
            font-size: 1.25rem;
            font-weight: 800;
            color: var(--ink-main);
            margin-top: 0.45rem;
            margin-bottom: 0.1rem;
        }
        .crest-note {
            font-size: 0.9rem;
            color: #333333;
            margin-bottom: 0.8rem;
        }
        .trail-label {
            font-size: 0.8rem;
            color: #555555;
            margin: 0.2rem 0 0.5rem 0.1rem;
        }
        .page-banner {
            background: linear-gradient(90deg, rgba(168,217,138,0.28) 0%, rgba(246,238,200,0.78) 100%);
            border: 1px solid var(--line-soft);
            border-radius: 18px;
            padding: 1.05rem 1rem 0.9rem 1rem;
            margin-bottom: 1.1rem;
            text-align: center;
            box-shadow: 0 4px 14px rgba(0,0,0,0.04);
        }
        .page-banner .title {
            font-size: 2.05rem;
            font-weight: 800;
            color: var(--ink-main);
            margin-bottom: 0.15rem;
        }
        .page-banner .subtitle {
            font-size: 1rem;
            font-weight: 600;
            color: #2d2d2d;
        }
        .panel-card {
            background: var(--card-wash);
            border: 1px solid var(--line-soft);
            border-radius: 18px;
            padding: 1rem;
            margin-bottom: 1rem;
            box-shadow: 0 4px 12px rgba(0,0,0,0.04);
        }
        .trail-item {
            display: block;
            width: 100%;
            text-align: left;
            padding: 0.7rem 0.85rem;
            margin-bottom: 0.45rem;
            border-radius: 12px;
            border: 1px solid var(--line-soft);
            background: rgba(255,255,255,0.72);
            color: var(--ink-main);
            font-weight: 600;
        }
        .trail-item.active {
            background: var(--mint-soft);
            border: 1px solid #94c973;
            box-shadow: 0 3px 10px rgba(148,201,115,0.15);
        }
        .tail-note {
            margin-top: 1.2rem;
            padding-top: 0.9rem;
            border-top: 1px solid rgba(0,0,0,0.12);
            text-align: center;
            font-size: 0.84rem;
            color: #333333;
        }
        .site-tail {
            margin-top: 1.8rem;
            padding: 1rem 0 0.5rem 0;
            text-align: center;
            font-size: 0.86rem;
            color: #333333;
            border-top: 1px solid var(--line-soft);
        }
        div.stButton > button {
            width: 100%;
            border-radius: 12px;
            border: 1px solid var(--line-soft);
            background: rgba(255,255,255,0.72);
            color: var(--ink-main);
            font-weight: 600;
            padding: 0.7rem 0.85rem;
            text-align: left;
        }
        div.stButton > button:hover {
            border-color: #94c973;
            color: var(--ink-main);
        }
        </style>
        """,
        unsafe_allow_html=True
    )

#Builds the top of the sidebar
def show_crest():
    crest = Path(MarkPath)
    with st.sidebar:
        st.markdown('<div class="crest-wrap">', unsafe_allow_html=True)
        if crest.exists():
            st.image(str(crest), width=170)
        else:
            st.warning("Logo file not found. Please add it to the app folder.")
        st.markdown(
            f"""
            <div class="crest-name">{AppTitle}</div>
            <div class="crest-note">Jamaican Banking Recommendation Assistant</div>
            """,
            unsafe_allow_html=True
        )
        st.markdown("</div>", unsafe_allow_html=True)

#Builds the sidebar menu and keeps the active page visible
def show_trail():
    st.sidebar.markdown('<div class="trail-label">Navigation</div>', unsafe_allow_html=True)
    pages = [
        "Landing Page",
        "Regular Chat",
        "Recommendation Generator",
        "Comparison Profile",
        "Dev Process",
        "Performance Metrics"
    ]
    for page in pages:
        active = page == st.session_state.current_view
        css_hook = "trail-item active" if active else "trail-item"
        st.sidebar.markdown(f'<div class="{css_hook}">{page}</div>', unsafe_allow_html=True)
        if st.sidebar.button(page, key=f"path_{page}"):
            st.session_state.current_view = page
            st.rerun()

#Builds the lower part of the sidebar
def show_trail_end():
    st.sidebar.markdown(
        f"""
        <div class="tail-note">
            <div><strong>{BuildTag}</strong></div>
            <div>{MakerLine}</div>
            <div style="margin-top:0.45rem;"><a href="{RepoLink}" target="_blank">GitHub Repository</a></div>
        </div>
        """,
        unsafe_allow_html=True
    )

#Builds the centered page header
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

#Builds the footer that will appear site wide
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

#Simple placeholder used until each section is built
def hold_page(title:str, text:str):
    show_banner(title)
    st.markdown(
        f"""
        <div class="panel-card">
            <h3 style="margin-top:0;">Coming Next</h3>
            <p style="margin-bottom:0;">{text}</p>
        </div>
        """,
        unsafe_allow_html=True
    )
    show_site_tail()

#Each page routes to its own display block
def open_landing():
    hold_page("Landing Page", "This is where the homepage, domain overview, full disclaimer, and usage guide will go.")

def open_chat():
    hold_page("Regular Chat", "This page will hold the standard chat interface and a clear chat control.")

def open_matcher():
    hold_page("Recommendation Generator", "This page will hold structured banking inputs on the left and recommendation results on the right.")

def open_compare():
    hold_page("Comparison Profile", "This page will hold comparison tools for banks and account types.")

def open_build():
    hold_page("Dev Process", "This page will outline the development process, key challenges, and the fixes used along the way.")

def open_scores():
    hold_page("Performance Metrics", "This page will show testing results, evaluation notes, and performance findings.")

#Sends the user to the correct section
def route_view(page_name:str):
    views = {
        "Landing Page": open_landing,
        "Regular Chat": open_chat,
        "Recommendation Generator": open_matcher,
        "Comparison Profile": open_compare,
        "Dev Process": open_build,
        "Performance Metrics": open_scores
    }
    views.get(page_name, open_landing)()

#Runs the shared app shell
def main():
    pour_style()
    show_crest()
    show_trail()
    show_trail_end()
    route_view(st.session_state.current_view)

if __name__ == "__main__":
    main()
