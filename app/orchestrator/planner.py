import streamlit as st
from datetime import date, timedelta

from app.memory.session_memory import mission


def render_current_step(step):

    if step == 0:
        destination_step()

    elif step == 1:
        dates_step()

    elif step == 2:
        travel_style_step()


def destination_step():

    st.subheader("Where would you like to travel?")

    destination = st.text_input(
        "Destination",
        placeholder="Japan"
    )

    if st.button("Next"):

        mission.update(
            "destination",
            destination
        )

        mission.execute_destination_agent()

        st.session_state.step = 1
        st.rerun()


def dates_step():

    st.subheader("When are you travelling?")

    dates = st.date_input(
        "Travel Dates",
        value=(
            date.today(),
            date.today() + timedelta(days=6)
        )
    )

    if st.button("Next"):

        mission.update(
            "dates",
            dates
        )

        st.session_state.step = 2
        st.rerun()


def travel_style_step():

    st.subheader("Who are you travelling with?")

    style = st.selectbox(
        "Travel Type",
        [
            "Solo",
            "Couple",
            "Family",
            "Friends",
            "Business"
        ]
    )

    if st.button("Continue"):

        mission.update(
            "travel_style",
            style
        )

        # Create initial city recommendations
        mission.execute_explorer_agent()

        # Creates the final route
        mission.execute_strategist_agent()

        st.success("Trip intelligence generated successfully.")