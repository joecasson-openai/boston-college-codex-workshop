import json
from pathlib import Path


DATA_PATH = Path(__file__).resolve().parents[1] / "data" / "study_spaces.json"


class StudySpacesService:
    service_name = "study_spaces"

    def __init__(self):
        with DATA_PATH.open() as handle:
            self.payload = json.load(handle)

    def list_spots(self) -> list[dict]:
        return self.payload["spots"]

    def search(self, vibe: str, need_whiteboard: bool) -> list[dict]:
        matches = []
        for spot in self.payload["spots"]:
            if vibe != spot["vibe"]:
                continue
            if need_whiteboard and not spot["whiteboard"]:
                continue
            matches.append(spot)
        return matches
