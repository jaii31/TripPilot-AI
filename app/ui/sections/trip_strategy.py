import streamlit as st


def render_trip_strategy(mission):

    recommendations = mission.get("recommendations") or {}
    strategy = mission.get("strategy") or {}

    cities = recommendations.get("cities", [])
    places = recommendations.get("places", [])

    st.divider()
    st.header("Your Trip Strategy")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            "Trip Type",
            strategy.get("trip_type", "Not available")
        )

    with col2:
        st.metric(
            "Travel Pace",
            strategy.get("travel_pace", "Not available")
        )

    with col3:
        st.metric(
            "Trip Duration",
            f"{mission.trip_length()} Days"
        )

    st.subheader("Recommended Route")

    route = strategy.get("recommended_route", cities)

    if route:
        st.info("  →  ".join(route))
    else:
        st.info("Route will be generated here.")

    st.subheader("Recommended Cities")

    if cities:

        city_columns = st.columns(len(cities))

        for column, city in zip(city_columns, cities):

            with column:
                st.markdown(
                    f"""
                    ### 📍 {city}
                    Recommended for your trip.
                    """
                )

    else:
        st.write("No city recommendations available.")

    st.subheader("Places to Explore")

    if places:

        place_columns = st.columns(2)

        for index, place in enumerate(places):

            with place_columns[index % 2]:

                st.markdown(
                    f"""
                    **✨ {place}**

                    Suggested by the Explorer Agent.
                    """
                )

    else:
        st.write("No attraction recommendations available.")

    days_per_city = strategy.get("days_per_city", {})

    if days_per_city:

        st.subheader("Suggested Stay")

        for city, days in days_per_city.items():

            st.write(
                f"📅 **{city}:** {days} day"
                f"{'s' if days != 1 else ''}"
            )