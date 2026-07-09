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

    elif step == 3:
        budget_step()


def destination_step():

    st.subheader(
        "Where would you like to travel?"
    )

    destination = st.text_input(
        "Destination",
        placeholder="Japan"
    )

    if st.button("Next"):

        if not destination.strip():

            st.error(
                "Enter a destination."
            )

            return

        mission.update(
            "destination",
            destination.strip()
        )

        mission.execute_destination_agent()

        st.session_state.step = 1

        st.rerun()


def dates_step():

    st.subheader(
        "When are you travelling?"
    )

    dates = st.date_input(

        "Travel Dates",

        value=(

            date.today(),

            date.today()
            + timedelta(days=6)
        )
    )

    if st.button("Next"):

        if len(dates) != 2:

            st.error(
                "Select a start and end date."
            )

            return

        mission.update(
            "dates",
            dates
        )

        st.session_state.step = 2

        st.rerun()


def travel_style_step():

    st.subheader(
        "Who are you travelling with?"
    )

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

        mission.execute_explorer_agent()

        mission.execute_strategist_agent()

        st.session_state.step = 3

        st.rerun()


def budget_step():

    st.subheader(
        "Plan your trip budget"
    )

    col1, col2 = st.columns(2)

    with col1:

        total_budget = st.number_input(

            "Total Trip Budget",

            min_value=1000,

            value=100000,

            step=5000
        )

    with col2:

        currency = st.selectbox(

            "Currency",

            [
                "INR",
                "USD",
                "EUR",
                "GBP",
                "JPY"
            ]
        )

    col3, col4 = st.columns(2)

    with col3:

        budget_style = st.selectbox(

            "Budget Preference",

            [
                "Economy",
                "Balanced",
                "Premium"
            ],

            index=1
        )

    with col4:

        travellers = st.number_input(

            "Number of Travellers",

            min_value=1,

            max_value=20,

            value=1
        )

    if st.button(
        "Generate Budget Plan"
    ):

        mission.update(

            "budget_input",

            {
                "total_budget":
                    total_budget,

                "currency":
                    currency,

                "budget_style":
                    budget_style,

                "travellers":
                    travellers
            }
        )

        mission.execute_budget_agent()

        st.success(
            "Budget plan generated."
        )