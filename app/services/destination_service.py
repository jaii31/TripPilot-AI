import json
from pathlib import Path


DATA_PATH = (
    Path(__file__).parent.parent
    / "data"
    / "country_profiles.json"
)


class DestinationService:

    def __init__(self):

        with open(DATA_PATH, encoding="utf-8") as file:
            self.database = json.load(file)

    def load_profile(self, country):

        return self.database.get(country)