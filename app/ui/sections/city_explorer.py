import streamlit as st

from app.services.explorer_service import ExplorerService


def render_city_explorer(mission):

    recommendations = mission.get("recommendations") or {}
    cities = recommendations.get("cities", [])

    if not cities:
        return

    # Existing service that reads city_profiles.json
    explorer_service = ExplorerService()

    st.divider()
    st.header("Explore Your Destinations")

    st.caption(
        "Discover experiences selected according to your route "
        "and travel style."
    )

    for city in cities:

        # Load this city's information from city_profiles.json
        city_data = explorer_service.load_city(city) or {}

        must_visit = city_data.get("must_visit", [])
        food = city_data.get("food", [])
        shopping = city_data.get("shopping", [])
        hidden_gems = city_data.get("hidden_gems", [])
        family = city_data.get("family", [])

        with st.expander(
            f"📍 Explore {city}",
            expanded=True
        ):

            st.subheader(city)

            col1, col2 = st.columns(2)

            with col1:

                st.markdown("### 🏛️ Must Visit")

                if must_visit:
                    for place in must_visit:
                        st.write(f"• {place}")
                else:
                    st.caption("No must-visit places available.")

                st.markdown("### 🍜 Local Food")

                if food:
                    for item in food:
                        st.write(f"• {item}")
                else:
                    st.caption("No food recommendations available.")

                st.markdown("### 🛍️ Shopping")

                if shopping:
                    for place in shopping:
                        st.write(f"• {place}")
                else:
                    st.caption("No shopping recommendations available.")

            with col2:

                st.markdown("### 💎 Hidden Gems")

                if hidden_gems:
                    for place in hidden_gems:
                        st.write(f"• {place}")
                else:
                    st.caption("No hidden gems available.")

                st.markdown("### 👨‍👩‍👧 Family Experiences")

                if family:
                    for place in family:
                        st.write(f"• {place}")
                else:
                    st.caption("No family experiences available.")