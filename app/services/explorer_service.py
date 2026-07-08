import json
from pathlib import Path


class ExplorerService:

    def __init__(self):

        self.base_path = (
            Path(__file__).resolve().parent.parent
            / "data"
            / "city_profiles.json"
        )

        with open(self.base_path, "r", encoding="utf-8") as f:
            self.data = json.load(f)

    def load_city(self, city):

        return self.data.get(city)