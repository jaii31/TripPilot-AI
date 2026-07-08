class StrategistService:

    def create_strategy(
        self,
        destination,
        days,
        travel_style,
        recommendations
    ):

        cities = recommendations.get("cities", [])

        if days <= 3:
            selected = cities[:1]

        elif days <= 6:
            selected = cities[:2]

        else:
            selected = cities[:3]

        days_per_city = {}

        if len(selected) > 0:

            remaining = days

            for city in selected[:-1]:
                allocation = max(2, days // len(selected))
                days_per_city[city] = allocation
                remaining -= allocation

            days_per_city[selected[-1]] = remaining

        return {

            "trip_type":
                "Single City"
                if len(selected) == 1
                else "Multi City",

            "recommended_route": selected,

            "days_per_city": days_per_city,

            "travel_pace":
                "Relaxed"
                if days >= 10
                else "Balanced",

            "travel_style": travel_style,

            "destination": destination
        }