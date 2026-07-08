import streamlit as st


def render_hero():

    st.markdown("<div class='hero-wrapper'>", unsafe_allow_html=True)

    st.markdown("<div class='hero-globe'>🌍</div>", unsafe_allow_html=True)

    st.markdown(
        "<div class='hero-badge'>Multi-Agent Travel Intelligence</div>",
        unsafe_allow_html=True,
    )

    st.markdown(
        "<h1 class='hero-title'>Where would you like to go?</h1>",
        unsafe_allow_html=True,
    )

    st.markdown(
        """
        <p class='hero-description'>
        Plan your journey with collaborative AI,
        real-time travel intelligence and transparent recommendations.
        </p>
        """,
        unsafe_allow_html=True,
    )

    st.text_input(
        "",
        placeholder="Search destination...",
        key="destination"
    )

    if st.button(
        "Continue →",
        key="continue",
    ):
        st.session_state.planner_started = True
        st.rerun()

    st.markdown("</div>", unsafe_allow_html=True)