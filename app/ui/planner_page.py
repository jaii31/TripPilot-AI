import streamlit as st
from app.orchestrator.planner import render_current_step
from app.memory.session_memory import mission


def render_planner_page():

    st.title("Plan Your Journey")

    progress = [
        "Destination",
        "Dates",
        "Travel Style",
        "Budget",
        "Transportation",
        "Accommodation",
        "Activities",
        "Weather",
        "Packing",
        "Summary"
    ]

    current_step = st.session_state.get("step", 0)

    cols = st.columns(len(progress))

    for i, col in enumerate(cols):

        with col:

            if i < current_step:
                st.success("✓")

            elif i == current_step:
                st.info(str(i + 1))

            else:
                st.write(str(i + 1))

            st.caption(progress[i])

    st.divider()

    render_current_step(current_step)

    st.divider()

    st.subheader("Mission State")

    st.json(mission.summary())