class AccommodationService:

    CITY_STAYS = {

        "Tokyo": {
            "Economy": {
                "type": "Budget Hotel",
                "area": "Asakusa",
                "nightly_cost": 4500,
                "examples": [
                    "Business hotel",
                    "Modern capsule hotel"
                ]
            },
            "Balanced": {
                "type": "Mid-range Hotel",
                "area": "Shinjuku",
                "nightly_cost": 8500,
                "examples": [
                    "Central city hotel",
                    "Boutique hotel"
                ]
            },
            "Premium": {
                "type": "Luxury Hotel",
                "area": "Ginza",
                "nightly_cost": 18000,
                "examples": [
                    "Luxury city hotel",
                    "Premium tower hotel"
                ]
            }
        },

        "Kyoto": {
            "Economy": {
                "type": "Guesthouse",
                "area": "Kyoto Station",
                "nightly_cost": 4000,
                "examples": [
                    "Traditional guesthouse",
                    "Budget city hotel"
                ]
            },
            "Balanced": {
                "type": "Boutique Hotel",
                "area": "Gion",
                "nightly_cost": 7500,
                "examples": [
                    "Machiya-style hotel",
                    "Central boutique stay"
                ]
            },
            "Premium": {
                "type": "Luxury Ryokan",
                "area": "Higashiyama",
                "nightly_cost": 17000,
                "examples": [
                    "Traditional ryokan",
                    "Luxury heritage stay"
                ]
            }
        },

        "Osaka": {
            "Economy": {
                "type": "Budget Hotel",
                "area": "Namba",
                "nightly_cost": 4000,
                "examples": [
                    "Compact city hotel",
                    "Budget business hotel"
                ]
            },
            "Balanced": {
                "type": "Mid-range Hotel",
                "area": "Dotonbori",
                "nightly_cost": 7000,
                "examples": [
                    "Central city hotel",
                    "Modern lifestyle hotel"
                ]
            },
            "Premium": {
                "type": "Luxury Hotel",
                "area": "Umeda",
                "nightly_cost": 15000,
                "examples": [
                    "Luxury tower hotel",
                    "Premium city resort"
                ]
            }
        },

        "Nara": {
            "Economy": {
                "type": "Guesthouse",
                "area": "Nara Station",
                "nightly_cost": 3500,
                "examples": [
                    "Local guesthouse",
                    "Budget inn"
                ]
            },
            "Balanced": {
                "type": "Comfort Hotel",
                "area": "Nara Park",
                "nightly_cost": 6000,
                "examples": [
                    "Park-side hotel",
                    "Traditional city hotel"
                ]
            },
            "Premium": {
                "type": "Luxury Ryokan",
                "area": "Naramachi",
                "nightly_cost": 13000,
                "examples": [
                    "Heritage ryokan",
                    "Luxury traditional stay"
                ]
            }
        }
    }

    def recommend(
        self,
        city,
        nights,
        budget_style,
        travellers
    ):

        city_data = self.CITY_STAYS.get(
            city,
            {}
        )

        stay = city_data.get(
            budget_style
        )

        if stay is None:

            stay = {
                "type": (
                    f"{budget_style} Accommodation"
                ),
                "area": "City Centre",
                "nightly_cost": 6000,
                "examples": [
                    "Recommended local hotel"
                ]
            }

        rooms = max(
            1,
            (travellers + 1) // 2
        )

        total_cost = (
            stay["nightly_cost"]
            * max(nights, 1)
            * rooms
        )

        return {
            "city": city,
            "nights": max(nights, 1),
            "rooms": rooms,
            "recommended_type":
                stay["type"],
            "recommended_area":
                stay["area"],
            "nightly_cost":
                stay["nightly_cost"],
            "estimated_total":
                total_cost,
            "examples":
                stay["examples"]
        }