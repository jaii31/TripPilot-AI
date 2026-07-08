import streamlit as st


def render_why_tripilot():

    st.markdown("<div class='why-wrapper'>", unsafe_allow_html=True)

    st.markdown(
        """
        <h2 class='section-title'>
            Why TripPilot?
        </h2>
        """,
        unsafe_allow_html=True,
    )

    st.markdown(
        """
        <p class='section-description'>
        Most travel planners generate an itinerary and expect you to follow it.
        TripPilot collaborates with you step by step, helping you make informed
        decisions while keeping you in complete control of your journey.
        </p>
        """,
        unsafe_allow_html=True,
    )

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("AI Specialists", "5")

    with col2:
        st.metric("Live Data Sources", "10+")

    with col3:
        st.metric("Planning Style", "Interactive")

    st.markdown("</div>", unsafe_allow_html=True)