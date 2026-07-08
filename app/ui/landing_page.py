import streamlit as st

from app.ui.styles import load_styles

from app.ui.sections.navbar import render_navbar
from app.ui.sections.hero import render_hero
from app.ui.sections.why_tripilot import render_why_tripilot
from app.ui.sections.workflow import render_workflow

from app.ui.planner_page import render_planner_page


def render_landing_page():

    st.set_page_config(
        page_title="TripPilot AI",
        page_icon="✈️",
        layout="wide",
    )

    load_styles()

    # -----------------------------
    # Planner Mode
    # -----------------------------
    if st.session_state.get("planner_started", False):

        render_navbar()
        render_planner_page()

        return

    # -----------------------------
    # Landing Page
    # -----------------------------
    render_navbar()

    render_hero()

    render_why_tripilot()

    render_workflow()