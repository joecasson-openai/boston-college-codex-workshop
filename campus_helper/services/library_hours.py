import json
from pathlib import Path


DATA_PATH = Path(__file__).resolve().parents[1] / "data" / "library_hours.json"


class LibraryHoursService:
    service_name = "library_hours"

    def __init__(self):
        with DATA_PATH.open() as handle:
            self.payload = json.load(handle)

    def get_hours(self, location_name: str, day: str) -> dict | None:
        for location in self.payload["locations"]:
            if location["location"] != location_name:
                continue
            return location["days"].get(day)
        return None
