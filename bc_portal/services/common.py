import json
from pathlib import Path


DATA_DIR = Path(__file__).resolve().parents[1] / "data"


def load_json(filename: str) -> dict:
    with (DATA_DIR / filename).open() as handle:
        return json.load(handle)
