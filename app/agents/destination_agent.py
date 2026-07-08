from app.agents.base_agent import BaseAgent
from app.services.geocoding_service import GeocodingService


class DestinationAgent(BaseAgent):

    def __init__(self):

        super().__init__("Destination Agent")

        self.geo = GeocodingService()

    def execute(self, mission):

        destination = mission.get("destination")

        result = self.geo.search(destination)

        if result is None:

            return {

                "status": "invalid_destination"

            }

        result["status"] = "validated"

        return result