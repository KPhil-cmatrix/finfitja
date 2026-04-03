"""
Developer: Khalia Phillips
App: FinFit JA
Version: 2.5
Purpose: Runs the main application shell and routes users across all platform sections.
"""

import streamlit as st
from layout import pour_style, show_crest, show_trail, show_trail_end
from pages.chat import open_chat
from pages.compare import open_compare
from pages.dev import open_build
from pages.home import open_landing
from pages.matcher import open_matcher
from pages.metrics import open_scores

#Configures main app settings
st.set_page_config(page_title="FinFit JA", page_icon="💵", layout="wide", initial_sidebar_state="expanded")

#Removes default Streamlit sidebar navigation
st.markdown(
    """
    <style>
    [data-testid="stSidebarNav"] {display: none;}
    </style>
    """,
    unsafe_allow_html=True
)

#Initializes current page state
if "current_view" not in st.session_state:
    st.session_state.current_view = "Home"

#Routes user to selected page
def route_view(page_name:str):
    views = {
        "Home": open_landing,
        "Ask FinFit": open_chat,
        "Recommendation Generator": open_matcher,
        "Comparison Profile": open_compare,
        "Development Overview": open_build,
        "Performance Metrics": open_scores
    }
    views.get(page_name, open_landing)()

#Runs full application shell
def main():
    pour_style()
    show_crest()
    show_trail()
    show_trail_end()
    route_view(st.session_state.current_view)

if __name__ == "__main__":
    main()