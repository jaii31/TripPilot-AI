import streamlit as st


def render_navbar():

    col1, col2 = st.columns([2, 1])

    with col1:
        st.markdown(
            "<h2 class='logo'>✈️ TripPilot AI</h2>",
            unsafe_allow_html=True
        )

    with col2:

        cols = st.columns(4)

        cols[0].markdown("<div class='nav-link'>About</div>", unsafe_allow_html=True)
        cols[1].markdown("<div class='nav-link'>Features</div>", unsafe_allow_html=True)
        cols[2].markdown("<div class='nav-link'>Workflow</div>", unsafe_allow_html=True)
        cols[3].markdown("<div class='nav-link'>GitHub</div>", unsafe_allow_html=True)

    st.divider()