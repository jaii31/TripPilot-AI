from app.services.transport_service import (
    TransportService
)


class TransportAgent:

    def __init__(self):

        self.service = TransportService()

    def execute(self, mission):

        strategy = mission.get("strategy") or {}

        route = strategy.get(
            "recommended_route",
            []
        )

        if len(route) < 2:

            return {
                "transportation": {
                    "routes": [],
                    "total_estimated_cost": 0
                }
            }

        routes = []

        total_cost = 0

        for index in range(
            len(route) - 1
        ):

            origin = route[index]

            destination = route[index + 1]

            transport = (
                self.service.get_route(
                    origin,
                    destination
                )
            )

            routes.append(
                transport
            )

            total_cost += (
                transport.get(
                    "estimated_cost",
                    0
                )
            )

        return {
            "transportation": {
                "routes": routes,
                "total_estimated_cost":
                    total_cost,
                "currency": "INR"
            }
        }