from geopy.geocoders import Nominatim


class GeocodingService:

    def __init__(self):

        self.geolocator = Nominatim(
            user_agent="TripPilotAI"
        )

    def search(self, place):

        location = self.geolocator.geocode(
            place,
            addressdetails=True
        )

        if location is None:
            return None

        address = location.raw.get("address", {})

        return {

            "query": place,

            "display_name": location.address,

            "latitude": location.latitude,

            "longitude": location.longitude,

            "country": address.get("country"),

            "country_code": address.get("country_code"),

            "state": address.get("state"),

            "city": (
                address.get("city")
                or address.get("town")
                or address.get("village")
            ),

        }