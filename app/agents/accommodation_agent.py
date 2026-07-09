from app.services.accommodation_service import (
    AccommodationService
)


class AccommodationAgent:

    def __init__(self):

        self.service = (
            AccommodationService()
        )

    def execute(self, mission):

        strategy = (
            mission.get("strategy")
            or {}
        )

        budget_input = (
            mission.get("budget_input")
            or {}
        )

        route = strategy.get(
            "recommended_route",
            []
        )

        days_per_city = strategy.get(
            "days_per_city",
            {}
        )

        budget_style = (
            budget_input.get(
                "budget_style",
                "Balanced"
            )
        )

        travellers = (
            budget_input.get(
                "travellers",
                1
            )
        )

        stays = []

        total_cost = 0

        for city in route:

            allocated_days = (
                days_per_city.get(
                    city,
                    1
                )
            )

            nights = max(
                allocated_days - 1,
                1
            )

            stay = (
                self.service.recommend(
                    city=city,
                    nights=nights,
                    budget_style=
                        budget_style,
                    travellers=
                        travellers
                )
            )

            stays.append(stay)

            total_cost += (
                stay["estimated_total"]
            )

        budget = (
            mission.get("budget")
            or {}
        )

        accommodation_budget = (
            budget
            .get("breakdown", {})
            .get("Accommodation", {})
            .get("amount", 0)
        )

        difference = (
            accommodation_budget
            - total_cost
        )

        if accommodation_budget == 0:

            status = (
                "Budget unavailable"
            )

        elif difference >= 0:

            status = (
                "Within budget"
            )

        else:

            status = (
                "Above budget"
            )

        return {
            "accommodation": {
                "stays": stays,
                "estimated_total":
                    total_cost,
                "allocated_budget":
                    accommodation_budget,
                "budget_difference":
                    difference,
                "budget_status":
                    status,
                "currency": "INR"
            }
        }