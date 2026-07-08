from app.services.destination_service import DestinationService


class ExplorerAgent:

    def __init__(self):
        self.service = DestinationService()

    def execute(self, mission):

        country = mission.get("destination")

        profile = self.service.load_profile(country)

        if profile is None:
            return {
                "recommendations": {
                    "cities": [],
                    "places": []
                }
            }

        style = mission.get("travel_style")

        cities = profile.get("cities", [])
        attractions = profile.get("attractions", [])

        if style == "Family":
            recommendations = {
                "cities": cities[:2],
                "places": attractions[:4]
            }

        elif style == "Solo":
            recommendations = {
                "cities": cities[1:4],
                "places": attractions[2:6]
            }

        elif style == "Couple":
            recommendations = {
                "cities": cities[:3],
                "places": attractions[:5]
            }

        elif style == "Business":
            recommendations = {
                "cities": cities[:2],
                "places": attractions[:2]
            }

        else:
            recommendations = {
                "cities": cities,
                "places": attractions
            }

        return {
            "recommendations": recommendations
        }