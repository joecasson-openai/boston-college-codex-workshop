import json
from pathlib import Path


DATA_PATH = Path(__file__).resolve().parents[1] / "data" / "dining_halls.json"


class DiningService:
    service_name = "dining"

    def __init__(self):
        with DATA_PATH.open() as handle:
            self.payload = json.load(handle)

    def list_halls(self) -> list[dict]:
        return self.payload["halls"]

    def get_hours(self, hall_name: str, day: str) -> dict | None:
        for hall in self.payload["halls"]:
            if hall["name"] != hall_name:
                continue
            today = hall["days"].get(day)
            if not today:
                return None
            return {
                "open_time": today["open"],
                "close_time": today["close"],
                "special": today["special"],
            }
        return None
