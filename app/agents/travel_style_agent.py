from app.memory.mission_control import MissionControl


VALID_STYLES = {
    "Solo",
    "Couple",
    "Family",
    "Friends",
    "Business"
}


class TravelStyleAgent:

    def run(self, style: str):

        style = style.strip().title()

        if style not in VALID_STYLES:
            return {
                "status": "error",
                "message": "Invalid travel style."
            }

        MissionControl.update(
            travel_style=style
        )

        return {
            "status": "success",
            "travel_style": style
        }