class Packwise:

    def execute(self, mission):

        weather = mission.get("weather") or {}

        weather_cities = weather.get(
            "cities",
            {}
        )

        travel_style = mission.get(
            "travel_style"
        )

        days = mission.trip_length()

        essentials = [
            "Passport / Government ID",
            "Wallet and travel cards",
            "Phone",
            "Phone charger",
            "Power bank",
            "Travel documents",
            "Reusable water bottle"
        ]

        clothing = [
            f"{days} comfortable outfits",
            f"{days + 1} pairs of innerwear",
            f"{days} pairs of socks",
            "Comfortable walking shoes",
            "Sleepwear"
        ]

        weather_items = []

        conditions = " ".join(

            str(
                city_weather.get(
                    "condition",
                    ""
                )
            ).lower()

            for city_weather
            in weather_cities.values()
        )

        rain_data = " ".join(

            str(
                city_weather.get(
                    "rain_chance",
                    ""
                )
            )

            for city_weather
            in weather_cities.values()
        )

        if (
            "rain" in conditions
            or "cloud" in conditions
        ):

            weather_items.extend(
                [
                    "Compact umbrella",
                    "Light waterproof jacket",
                    "Quick-dry clothing"
                ]
            )

        if (
            "sun" in conditions
            or "warm" in conditions
        ):

            weather_items.extend(
                [
                    "Sunscreen",
                    "Sunglasses",
                    "Cap or sun hat",
                    "Breathable clothing"
                ]
            )

        if not weather_items:

            weather_items.extend(
                [
                    "Light jacket",
                    "Weather-appropriate clothing"
                ]
            )

        personal_items = [
            "Toiletries",
            "Personal medicines",
            "Hand sanitizer",
            "Tissues",
            "Small first-aid kit"
        ]

        electronics = [
            "Charging cables",
            "Universal travel adapter",
            "Earphones or headphones"
        ]

        travel_specific = []

        if travel_style == "Solo":

            travel_specific = [
                "Emergency contact information",
                "Secure cross-body bag",
                "Portable safety alarm"
            ]

        elif travel_style == "Couple":

            travel_specific = [
                "Shared document pouch",
                "Camera",
                "Compact day bag"
            ]

        elif travel_style == "Family":

            travel_specific = [
                "Family medicines",
                "Snacks",
                "Wet wipes",
                "Entertainment for children"
            ]

        elif travel_style == "Friends":

            travel_specific = [
                "Shared power bank",
                "Portable speaker",
                "Group emergency contacts"
            ]

        elif travel_style == "Business":

            travel_specific = [
                "Laptop",
                "Laptop charger",
                "Formal outfit",
                "Business documents"
            ]

        packing = {

            "trip_duration": days,

            "travel_style": travel_style,

            "categories": {

                "Essentials":
                    essentials,

                "Clothing":
                    clothing,

                "Weather Ready":
                    weather_items,

                "Personal Care":
                    personal_items,

                "Electronics":
                    electronics,

                "Travel Specific":
                    travel_specific
            }
        }

        total_items = sum(

            len(items)

            for items
            in packing[
                "categories"
            ].values()
        )

        packing[
            "total_items"
        ] = total_items

        packing[
            "status"
        ] = "generated"

        return {

            "packing": packing
        }