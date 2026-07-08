from app.services.strategist_service import StrategistService


class Strategist:

    def __init__(self):
        self.service = StrategistService()

    def execute(self, mission):

        strategy = self.service.create_strategy(
            destination=mission.get("destination"),
            days=mission.trip_length(),
            travel_style=mission.get("travel_style"),
            recommendations=mission.get("recommendations"),
        )

        return {
            "strategy": strategy
        }