import json
import streamlit as st

from app.memory.session_memory import mission
from app.ui.trip_copilot import render_trip_copilot


def render_trip_summary():

    data = mission.summary()

    destination = data.get(
        "destination",
        "Your Destination"
    )

    dates = data.get(
        "dates",
        []
    )

    travel_style = data.get(
        "travel_style",
        "Balanced"
    )

    recommendations = (
        data.get("recommendations")
        or {}
    )

    cities = recommendations.get(
        "cities",
        []
    )

    strategy = (
        data.get("strategy")
        or {}
    )

    budget = (
        data.get("budget_plan")
        or data.get("budget")
        or {}
    )

    transportation = (
        data.get("transportation_plan")
        or data.get("transportation")
        or {}
    )

    accommodation = (
        data.get("accommodation_plan")
        or data.get("accommodation")
        or {}
    )

    activities = (
        data.get("activities")
        or {}
    )

    weather = (
        data.get("weather")
        or {}
    )

    packing = (
        data.get("packing")
        or data.get("packing_plan")
        or {}
    )

    trip_days = mission.trip_length()

    # -----------------------------------
    # HEADER
    # -----------------------------------

    st.divider()

    st.title(
        f"✈️ Your {destination} Journey"
    )

    st.caption(
        "Your complete AI-generated travel "
        "plan is ready."
    )

    # -----------------------------------
    # TRIP OVERVIEW
    # -----------------------------------

    col1, col2, col3, col4 = (
        st.columns(4)
    )

    with col1:

        st.metric(
            "Destination",
            destination
        )

    with col2:

        st.metric(
            "Trip Duration",
            f"{trip_days} Days"
        )

    with col3:

        st.metric(
            "Travel Style",
            travel_style
        )

    with col4:

        st.metric(
            "Cities",
            len(cities)
        )

    if (
        isinstance(dates, (tuple, list))
        and len(dates) == 2
    ):

        st.info(
            f"📅 {dates[0].strftime('%d %B %Y')} "
            f"→ "
            f"{dates[1].strftime('%d %B %Y')}"
        )

    # -----------------------------------
    # ROUTE
    # -----------------------------------

    st.subheader(
        "🗺️ Your Journey Route"
    )

    if cities:

        route = "  →  ".join(cities)

        st.success(
            route
        )

    else:

        st.write(
            destination
        )

    # -----------------------------------
    # DAY-BY-DAY ITINERARY
    # -----------------------------------

    st.subheader(
        "📆 Day-by-Day Journey"
    )

    activity_list = []

    if isinstance(
        activities,
        dict
    ):

        for city, city_activities in (
            activities.items()
        ):

            if isinstance(
                city_activities,
                list
            ):

                for activity in (
                    city_activities
                ):

                    if isinstance(
                        activity,
                        dict
                    ):

                        activity_list.append(
                            {
                                "city": city,
                                "name":
                                    activity.get(
                                        "name",
                                        "Explore"
                                    )
                            }
                        )

    for day in range(
        1,
        trip_days + 1
    ):

        city = (

            cities[
                (day - 1)
                % len(cities)
            ]

            if cities

            else destination
        )

        with st.expander(
            f"Day {day} — {city}",
            expanded=day == 1
        ):

            day_items = [

                item

                for item
                in activity_list

                if item["city"]
                == city

            ]

            if day_items:

                item = day_items[
                    (day - 1)
                    % len(day_items)
                ]

                st.markdown(
                    f"### 📍 "
                    f"{item['name']}"
                )

            else:

                st.markdown(
                    "### 📍 Explore "
                    f"{city}"
                )

            st.write(
                "Discover local attractions, "
                "culture and experiences."
            )

            st.caption(
                "TripPilot recommends keeping "
                "some flexible time for local "
                "discoveries."
            )

    # -----------------------------------
    # INTELLIGENCE SUMMARY
    # -----------------------------------

    st.subheader(
        "🧠 Trip Intelligence"
    )

    tab1, tab2, tab3, tab4 = (
        st.tabs(
            [
                "🚆 Travel",
                "🏨 Stay",
                "🌤️ Weather",
                "🎒 Packing"
            ]
        )
    )

    with tab1:

        if transportation:

            st.write(
                "Your optimized route and "
                "transport recommendations "
                "are included in the complete "
                "plan above."
            )

        else:

            st.info(
                "Transportation recommendations "
                "are ready."
            )

    with tab2:

        if accommodation:

            st.write(
                "Accommodation recommendations "
                "have been selected according "
                "to your destination and budget."
            )

        else:

            st.info(
                "Accommodation intelligence "
                "is ready."
            )

    with tab3:

        if weather:

            st.write(
                "Weather conditions have been "
                "considered while preparing "
                "your activities and packing "
                "recommendations."
            )

        else:

            st.info(
                "Weather intelligence is ready."
            )

    with tab4:

        if packing:

            st.write(
                "Your personalized Packwise "
                "checklist is included above."
            )

        else:

            st.info(
                "Your packing checklist "
                "is ready."
            )

    # -----------------------------------
    # TRIP READINESS
    # -----------------------------------

    st.subheader(
        "🚀 Trip Readiness"
    )

    completed = 0

    checks = [

        bool(destination),

        bool(dates),

        bool(cities),

        bool(budget),

        bool(transportation),

        bool(accommodation),

        bool(activities),

        bool(weather),

        bool(packing)

    ]

    completed = sum(checks)

    readiness = int(
        completed
        / len(checks)
        * 100
    )

    st.progress(
        readiness / 100
    )

    st.metric(
        "Trip Readiness Score",
        f"{readiness}%"
    )

    if readiness >= 80:

        st.success(
            "Your journey is ready. "
            "Have an amazing trip! ✈️"
        )

    else:

        st.warning(
            "Your core journey is ready. "
            "Review the recommendations "
            "before travelling."
        )

    # -----------------------------------
    # DOWNLOAD
    # -----------------------------------

    st.subheader(
        "📥 Save Your Journey"
    )

    export_data = {

        "destination":
            destination,

        "dates": [
            str(item)
            for item in dates
        ],

        "travel_style":
            travel_style,

        "trip_duration":
            trip_days,

        "cities":
            cities,

        "trip_plan":
            data

    }

    itinerary_json = (
        json.dumps(
            export_data,
            indent=4,
            default=str
        )
    )

    st.download_button(

        label=(
            "⬇️ Download Complete "
            "Trip Plan"
        ),

        data=itinerary_json,

        file_name=(
            "TripPilot_"
            f"{destination}"
            "_Journey.json"
        ),

        mime=(
            "application/json"
        ),

        use_container_width=True
    )

    st.success(
        "TripPilot AI has completed "
        "your personalized journey."
    )

    st.divider()

    render_trip_copilot()

    if st.button(
        "✈️ Plan Another Journey",
        use_container_width=True
    ):
        mission.state.clear()

        for key in list(st.session_state.keys()):
            del st.session_state[key]

        st.session_state.step = 0

        st.rerun()