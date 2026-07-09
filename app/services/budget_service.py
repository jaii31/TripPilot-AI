class BudgetService:

    def create_budget_plan(
        self,
        total_budget,
        currency,
        budget_style,
        days,
        travellers
    ):

        if budget_style == "Economy":
            allocation = {
                "Transportation": 25,
                "Accommodation": 25,
                "Food": 18,
                "Activities": 12,
                "Local Travel": 10,
                "Emergency Reserve": 10
            }

        elif budget_style == "Premium":
            allocation = {
                "Transportation": 25,
                "Accommodation": 35,
                "Food": 18,
                "Activities": 12,
                "Local Travel": 5,
                "Emergency Reserve": 5
            }

        else:
            allocation = {
                "Transportation": 25,
                "Accommodation": 30,
                "Food": 18,
                "Activities": 12,
                "Local Travel": 8,
                "Emergency Reserve": 7
            }

        breakdown = {}

        for category, percentage in allocation.items():

            breakdown[category] = {
                "percentage": percentage,
                "amount": round(
                    total_budget * percentage / 100,
                    2
                )
            }

        return {
            "total_budget": total_budget,
            "currency": currency,
            "budget_style": budget_style,
            "trip_days": days,
            "travellers": travellers,
            "daily_budget": round(
                total_budget / max(days, 1),
                2
            ),
            "budget_per_person": round(
                total_budget / max(travellers, 1),
                2
            ),
            "breakdown": breakdown
        }