import streamlit as st


def render_weather_plan(mission):

    weather = (
        mission.get("weather") or {}
    )

    cities = weather.get(
        "cities",
        {}
    )

    if not cities:

        return

    st.divider()

    st.header(
        "Weather Intelligence"
    )

    st.caption(
        "Destination weather insights "
        "for your planned journey."
    )

    columns = st.columns(
        min(len(cities), 3)
    )

    for index, (
        city,
        forecast
    ) in enumerate(
        cities.items()
    ):

        column = columns[
            index % len(columns)
        ]

        with column:

            with st.container(
                border=True
            ):

                st.subheader(
                    f"🌤️ {city}"
                )

                st.metric(
                    "Temperature",

                    forecast.get(
                        "temperature",
                        "Unavailable"
                    )
                )

                st.write(
                    "**Condition:** "
                    + forecast.get(
                        "condition",
                        "Unavailable"
                    )
                )

                st.write(
                    "**Rain Chance:** "
                    + forecast.get(
                        "rain_chance",
                        "Unavailable"
                    )
                )

                st.write(
                    "**Humidity:** "
                    + forecast.get(
                        "humidity",
                        "Unavailable"
                    )
                )

                st.info(
                    forecast.get(
                        "recommendation",
                        "Check local weather "
                        "before travelling."
                    )
                )