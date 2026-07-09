import streamlit as st


def render_transport_result(mission):

    transportation = (
        mission.get("transportation")
        or {}
    )

    routes = transportation.get(
        "routes",
        []
    )

    if not routes:

        return

    st.divider()

    st.header(
        "Transportation Plan"
    )

    st.caption(
        "Recommended connections selected "
        "for your planned route."
    )

    total_cost = (
        transportation.get(
            "total_estimated_cost",
            0
        )
    )

    col1, col2 = st.columns(2)

    with col1:

        st.metric(
            "Route Connections",
            len(routes)
        )

    with col2:

        st.metric(
            "Estimated Intercity Cost",
            f"₹{total_cost:,.0f}"
        )

    for route in routes:

        origin = route.get(
            "origin"
        )

        destination = route.get(
            "destination"
        )

        with st.container(
            border=True
        ):

            st.subheader(
                f"{origin} → {destination}"
            )

            col1, col2, col3 = (
                st.columns(3)
            )

            with col1:

                st.metric(
                    "Recommended",
                    route.get(
                        "recommended_mode"
                    )
                )

            with col2:

                st.metric(
                    "Travel Time",
                    route.get(
                        "duration"
                    )
                )

            with col3:

                st.metric(
                    "Estimated Cost",
                    (
                        f"₹"
                        f"{route.get('estimated_cost', 0):,.0f}"
                    )
                )

            st.caption(
                f"Distance: "
                f"{route.get('distance')}"
            )

            st.info(
                route.get(
                    "reason"
                )
            )

            alternatives = (
                route.get(
                    "alternatives",
                    []
                )
            )

            if alternatives:

                with st.expander(
                    "Compare alternatives"
                ):

                    for option in alternatives:

                        st.write(
                            f"**{option.get('mode')}**"
                            f" — "
                            f"{option.get('duration')}"
                            f" — "
                            f"₹"
                            f"{option.get('estimated_cost', 0):,.0f}"
                        )