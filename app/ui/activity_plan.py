import streamlit as st


def render_activity_plan(mission):

    activities = mission.get("activities") or {}

    if not activities:
        return

    st.divider()
    st.header("Activities Plan")

    st.caption(
        "Personalized experiences selected for your route."
    )

    total_cost = 0

    for city, city_activities in activities.items():

        st.subheader(f"📍 {city}")

        if not city_activities:

            st.info(
                "No activities available for this destination."
            )

            continue

        columns = st.columns(2)

        for index, activity in enumerate(
            city_activities
        ):

            estimated_cost = activity.get(
                "estimated_cost",
                0
            )

            total_cost += estimated_cost

            with columns[index % 2]:

                with st.container(border=True):

                    st.markdown(
                        f"### {activity.get('name')}"
                    )

                    st.caption(
                        activity.get(
                            "category",
                            "Experience"
                        )
                    )

                    col1, col2 = st.columns(2)

                    with col1:

                        st.metric(
                            "Duration",
                            activity.get(
                                "duration",
                                "Not available"
                            )
                        )

                    with col2:

                        st.metric(
                            "Estimated Cost",
                            f"₹{estimated_cost:,}"
                        )

    st.subheader(
        f"Estimated Activities Cost: ₹{total_cost:,}"
    )