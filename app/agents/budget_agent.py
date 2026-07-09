from app.services.budget_service import BudgetService


class BudgetAgent:

    def __init__(self):

        self.service = BudgetService()

    def execute(self, mission):

        budget_data = mission.get("budget_input")

        if not budget_data:
            return {
                "budget": {}
            }

        budget = self.service.create_budget_plan(

            total_budget=budget_data.get(
                "total_budget",
                0
            ),

            currency=budget_data.get(
                "currency",
                "INR"
            ),

            budget_style=budget_data.get(
                "budget_style",
                "Balanced"
            ),

            days=mission.trip_length(),

            travellers=budget_data.get(
                "travellers",
                1
            )
        )

        return {
            "budget": budget
        }