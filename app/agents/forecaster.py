class Forecaster:

    def execute(self, mission):

        recommendations = (
            mission.get("recommendations") or {}
        )

        cities = recommendations.get(
            "cities",
            []
        )

        dates = mission.get("dates")

        if not cities:

            return {
                "weather": {
                    "cities": {},
                    "status": "unavailable"
                }
            }

        weather_profiles = {

            "Tokyo": {
                "condition": "Partly Cloudy",
                "temperature": "24°C – 30°C",
                "rain_chance": "35%",
                "humidity": "72%",
                "recommendation":
                    "Carry a light umbrella and "
                    "wear breathable clothing."
            },

            "Kyoto": {
                "condition": "Warm and Sunny",
                "temperature": "25°C – 32°C",
                "rain_chance": "25%",
                "humidity": "68%",
                "recommendation":
                    "Plan outdoor attractions "
                    "during the morning."
            },

            "Osaka": {
                "condition": "Partly Sunny",
                "temperature": "25°C – 31°C",
                "rain_chance": "30%",
                "humidity": "70%",
                "recommendation":
                    "Keep water available during "
                    "outdoor exploration."
            },

            "Nara": {
                "condition": "Sunny",
                "temperature": "24°C – 31°C",
                "rain_chance": "20%",
                "humidity": "65%",
                "recommendation":
                    "Suitable weather for parks "
                    "and outdoor attractions."
            }
        }

        city_forecasts = {}

        for city in cities:

            city_forecasts[city] = (
                weather_profiles.get(
                    city,
                    {
                        "condition":
                            "Weather data unavailable",

                        "temperature":
                            "Not available",

                        "rain_chance":
                            "Not available",

                        "humidity":
                            "Not available",

                        "recommendation":
                            "Check local weather "
                            "before travelling."
                    }
                )
            )

        return {

            "weather": {

                "trip_dates": dates,

                "cities": city_forecasts,

                "status": "generated"
            }
        }