import streamlit as st


def render_workflow():

    st.header("How TripPilot Works")

    steps = [
        ("1", "Choose Destination"),
        ("2", "Select Travel Dates"),
        ("3", "Customize Your Trip"),
        ("4", "AI Collaborates With You"),
        ("5", "Receive Your Final Plan"),
    ]

    cols = st.columns(len(steps))

    for col, (num, title) in zip(cols, steps):
        with col:
            st.markdown(f"### {num}")
            st.write(title)