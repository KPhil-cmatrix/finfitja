"""
Developer's Name: Khalia Phillips
App Name: FinFit JA
Version: 2.2
Purpose (File): This file runs the main FinFit JA Streamlit app and routes users between the different sections of the platform.
"""

import streamlit as st
from layout import pour_style, show_crest, show_trail, show_trail_end
from pages.home import open_landing
from pages.chat import open_chat
from pages.matcher import open_matcher
from pages.compare import open_compare
from pages.dev import open_build
from pages.metrics import open_scores

st.set_page_config(page_title="FinFit JA", page_icon="💵", layout="wide", initial_sidebar_state="expanded")

#Removes Streamlit automatic page navigation
st.markdown(
    """
    <style>
    [data-testid="stSidebarNav"] {display: none;}
    </style>
    """,
    unsafe_allow_html=True
)

#Keeps track of the page the user is currently on
if "current_view" not in st.session_state:
    st.session_state.current_view = "Home"

#Routes the user to the correct page
def route_view(page_name:str):
    views = {
        "Home": open_landing,
        "Ask FinFit": open_chat,
        "Recommendation Generator": open_matcher,
        "Comparison Profile": open_compare,
        "Dev Process": open_build,
        "Performance Metrics": open_scores
    }
    views.get(page_name, open_landing)()

#Runs the app shell
def main():
    pour_style()
    show_crest()
    show_trail()
    show_trail_end()
    route_view(st.session_state.current_view)

if __name__ == "__main__":
    main()
