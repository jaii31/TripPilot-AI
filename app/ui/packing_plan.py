import streamlit as st


def render_packing_plan(mission):

    packing = (
        mission.get("packing") or {}
    )

    categories = packing.get(
        "categories",
        {}
    )

    if not categories:

        return

    st.divider()

    st.header(
        "Packwise Checklist"
    )

    st.caption(
        "A personalized packing plan "
        "based on your destination, "
        "weather, trip duration and "
        "travel style."
    )

    col1, col2, col3 = (
        st.columns(3)
    )

    col1.metric(

        "Trip Duration",

        f"""
        {
            packing.get(
                "trip_duration",
                1
            )
        } Days
        """
    )

    col2.metric(

        "Travel Type",

        packing.get(
            "travel_style",
            "Traveller"
        )
    )

    col3.metric(

        "Packing Items",

        packing.get(
            "total_items",
            0
        )
    )

    category_icons = {

        "Essentials": "🎒",

        "Clothing": "👕",

        "Weather Ready": "🌦️",

        "Personal Care": "🧴",

        "Electronics": "🔌",

        "Travel Specific": "🧭"
    }

    category_names = list(
        categories.keys()
    )

    for index in range(
        0,
        len(category_names),
        2
    ):

        columns = st.columns(2)

        current_categories = (
            category_names[
                index:index + 2
            ]
        )

        for column, category in zip(

            columns,

            current_categories
        ):

            items = categories.get(
                category,
                []
            )

            with column:

                with st.container(
                    border=True
                ):

                    icon = (
                        category_icons.get(
                            category,
                            "✓"
                        )
                    )

                    st.subheader(
                        f"{icon} {category}"
                    )

                    if not items:

                        st.caption(
                            "No additional items "
                            "required."
                        )

                    for item_index, item in (
                        enumerate(items)
                    ):

                        st.checkbox(

                            item,

                            key=(

                                "packing_"

                                + category

                                + "_"

                                + str(
                                    item_index
                                )
                            )
                        )