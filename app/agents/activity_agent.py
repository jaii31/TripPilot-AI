from app.services.explorer_service import ExplorerService


class ActivityAgent:

    def __init__(self):

        self.service = ExplorerService()

    def execute(self, mission):

        strategy = mission.get("strategy") or {}

        route = strategy.get(
            "recommended_route",
            []
        )

        travel_style = mission.get(
            "travel_style"
        )

        activities = {}

        for city in route:

            city_data = (
                self.service.load_city(city)
                or {}
            )

            selected = []

            selected.extend(
                self.build_activities(
                    city_data.get(
                        "must_visit",
                        []
                    )[:2],
                    "Sightseeing"
                )
            )

            selected.extend(
                self.build_activities(
                    city_data.get(
                        "hidden_gems",
                        []
                    )[:1],
                    "Hidden Gem"
                )
            )

            if travel_style == "Family":

                selected.extend(
                    self.build_activities(
                        city_data.get(
                            "family",
                            []
                        )[:1],
                        "Family Experience"
                    )
                )

            activities[city] = selected

        total_activities = sum(
            len(items)
            for items in activities.values()
        )

        return {
            "activities": activities,

            "activity_summary": {
                "cities_covered":
                    len(activities),

                "total_activities":
                    total_activities
            }
        }

    def build_activities(
        self,
        places,
        category
    ):

        return [

            {
                "name": place,

                "category": category,

                "duration":
                    self.get_duration(
                        category
                    ),

                "estimated_cost":
                    self.get_cost(
                        category
                    )
            }

            for place in places
        ]

    def get_duration(
        self,
        category
    ):

        durations = {

            "Sightseeing":
                "2–3 hours",

            "Hidden Gem":
                "1–2 hours",

            "Family Experience":
                "3–4 hours"
        }

        return durations.get(
            category,
            "2 hours"
        )

    def get_cost(
        self,
        category
    ):

        costs = {

            "Sightseeing": 1500,

            "Hidden Gem": 800,

            "Family Experience": 2500
        }

        return costs.get(
            category,
            1000
        )