class TransportService:

    ROUTES = {

        ("Kyoto", "Osaka"): {
            "recommended_mode": "Train",
            "duration": "30 minutes",
            "estimated_cost": 900,
            "distance": "56 km",
            "reason": (
                "Fast, frequent and convenient "
                "for travel between Kyoto and Osaka."
            ),
            "alternatives": [
                {
                    "mode": "Bus",
                    "duration": "1 hour 20 minutes",
                    "estimated_cost": 700
                },
                {
                    "mode": "Car",
                    "duration": "1 hour",
                    "estimated_cost": 2500
                }
            ]
        },

        ("Osaka", "Nara"): {
            "recommended_mode": "Train",
            "duration": "45 minutes",
            "estimated_cost": 500,
            "distance": "32 km",
            "reason": (
                "Train provides the fastest and "
                "most economical connection."
            ),
            "alternatives": [
                {
                    "mode": "Bus",
                    "duration": "1 hour 15 minutes",
                    "estimated_cost": 600
                },
                {
                    "mode": "Car",
                    "duration": "50 minutes",
                    "estimated_cost": 1800
                }
            ]
        },

        ("Tokyo", "Kyoto"): {
            "recommended_mode": "Shinkansen",
            "duration": "2 hours 15 minutes",
            "estimated_cost": 7500,
            "distance": "450 km",
            "reason": (
                "Shinkansen offers the best balance "
                "of speed, comfort and reliability."
            ),
            "alternatives": [
                {
                    "mode": "Flight",
                    "duration": "3 hours 30 minutes",
                    "estimated_cost": 9000
                },
                {
                    "mode": "Bus",
                    "duration": "8 hours",
                    "estimated_cost": 3500
                }
            ]
        }
    }

    def get_route(self, origin, destination):

        route = self.ROUTES.get(
            (origin, destination)
        )

        if route:

            return {
                "origin": origin,
                "destination": destination,
                **route
            }

        return {
            "origin": origin,
            "destination": destination,
            "recommended_mode": "Train",
            "duration": "Estimate unavailable",
            "estimated_cost": 0,
            "distance": "Estimate unavailable",
            "reason": (
                "Train selected as the default "
                "intercity transport option."
            ),
            "alternatives": []
        }