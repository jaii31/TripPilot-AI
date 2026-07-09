import streamlit as st


def render_accommodation_result(
    mission
):

    accommodation = (
        mission.get(
            "accommodation"
        )
        or {}
    )

    stays = accommodation.get(
        "stays",
        []
    )

    if not stays:

        return

    st.divider()

    st.header(
        "Accommodation Plan"
    )

    st.caption(
        "Stay recommendations selected "
        "for your route and budget style."
    )

    total = accommodation.get(
        "estimated_total",
        0
    )

    allocated = accommodation.get(
        "allocated_budget",
        0
    )

    status = accommodation.get(
        "budget_status",
        "Unavailable"
    )

    col1, col2, col3 = (
        st.columns(3)
    )

    with col1:

        st.metric(
            "Estimated Stay Cost",
            f"₹{total:,.0f}"
        )

    with col2:

        st.metric(
            "Accommodation Budget",
            f"₹{allocated:,.0f}"
        )

    with col3:

        st.metric(
            "Budget Status",
            status
        )

    if status == "Within budget":

        st.success(
            "The recommended stays fit "
            "within your accommodation budget."
        )

    elif status == "Above budget":

        difference = abs(
            accommodation.get(
                "budget_difference",
                0
            )
        )

        st.warning(
            "Estimated accommodation is "
            f"₹{difference:,.0f} above "
            "the allocated budget."
        )

    for stay in stays:

        with st.container(
            border=True
        ):

            st.subheader(
                f"🏨 {stay.get('city')}"
            )

            col1, col2, col3 = (
                st.columns(3)
            )

            with col1:

                st.caption(
                    "Recommended Stay"
                )

                st.write(
                    f"**"
                    f"{stay.get('recommended_type')}"
                    f"**"
                )

            with col2:

                st.caption(
                    "Best Area"
                )

                st.write(
                    f"**"
                    f"{stay.get('recommended_area')}"
                    f"**"
                )

            with col3:

                st.caption(
                    "Estimated Cost"
                )

                st.write(
                    f"**₹"
                    f"{stay.get('estimated_total', 0):,.0f}"
                    f"**"
                )

            st.write(
                f"🌙 {stay.get('nights')} nights"
                f"  •  "
                f"🛏️ {stay.get('rooms')} room(s)"
                f"  •  "
                f"₹"
                f"{stay.get('nightly_cost', 0):,.0f}"
                f" per room/night"
            )

            examples = stay.get(
                "examples",
                []
            )

            if examples:

                st.caption(
                    "Suggested stay categories"
                )

                for example in examples:

                    st.write(
                        f"• {example}"
                    )