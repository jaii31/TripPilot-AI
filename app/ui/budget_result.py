import streamlit as st


CURRENCY_SYMBOLS = {
    "INR": "₹",
    "USD": "$",
    "EUR": "€",
    "GBP": "£",
    "JPY": "¥"
}


def render_budget_result(mission):

    budget = mission.get("budget") or {}

    if not budget:
        return

    symbol = CURRENCY_SYMBOLS.get(
        budget.get("currency"),
        ""
    )

    st.divider()

    st.header("Your Budget Plan")

    col1, col2, col3 = st.columns(3)

    with col1:

        st.caption("Total Trip Budget")

        st.subheader(
            f"{symbol}"
            f"{budget.get('total_budget', 0):,.0f}"
        )

    with col2:

        st.caption("Daily Budget")

        st.subheader(
            f"{symbol}"
            f"{budget.get('daily_budget', 0):,.0f}"
        )

    with col3:

        st.caption("Budget Per Person")

        st.subheader(
            f"{symbol}"
            f"{budget.get('budget_per_person', 0):,.0f}"
        )

    st.subheader("Suggested Allocation")

    breakdown = budget.get(
        "breakdown",
        {}
    )

    for category, details in breakdown.items():

        amount = details.get(
            "amount",
            0
        )

        percentage = details.get(
            "percentage",
            0
        )

        st.markdown(
            f"**{category} — "
            f"{symbol}{amount:,.0f} "
            f"({percentage}%)**"
        )

        st.progress(
            percentage / 100
        )