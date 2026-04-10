from __future__ import annotations

import json
import threading
from pathlib import Path
from difflib import get_close_matches
from typing import Optional

from bc_portal.services.common import DATA_DIR


CACHE_PATH = DATA_DIR / "eagleeval_cache.json"


# Mock dataset to simulate EagleEval entries. In a real integration this would
# be replaced by a scraper or API client that queries eagleeval.com.
_MOCK_DATA = {
    "CSCI1102": {"homeworkHours": 8, "difficulty": 3.5},
    "MATH2210": {"homeworkHours": 6, "difficulty": 4.0},
    "ENGL1080": {"homeworkHours": 3, "difficulty": 2.5},
    "ACCT1021": {"homeworkHours": 5, "difficulty": 3.0},
    "ISYS3257": {"homeworkHours": 7, "difficulty": 3.7},
    "MKTG2150": {"homeworkHours": 4, "difficulty": 2.8},
}


def _load_cache() -> dict:
    try:
        if CACHE_PATH.exists():
            with CACHE_PATH.open() as fh:
                return json.load(fh)
    except Exception:
        # Fail silently if cache corrupt/unreadable
        return {}
    return {}


def _save_cache(cache: dict) -> None:
    try:
        with CACHE_PATH.open("w") as fh:
            json.dump(cache, fh)
    except Exception:
        # Don't raise; caching is best-effort
        pass


def _normalize(code: str) -> str:
    return "".join(code.split()).upper()


def _fetch_from_source(course_code: str) -> Optional[dict]:
    # Simulated remote lookup using mock data and fuzzy matching.
    key = _normalize(course_code)
    if key in _MOCK_DATA:
        return _MOCK_DATA[key]

    # Fuzzy match against mock keys
    candidates = get_close_matches(key, list(_MOCK_DATA.keys()), n=1, cutoff=0.6)
    if candidates:
        return _MOCK_DATA[candidates[0]]
    return None


def _background_fetch_and_cache(course_code: str) -> None:
    try:
        result = _fetch_from_source(course_code)
        if result is None:
            return
        cache = _load_cache()
        cache[_normalize(course_code)] = result
        _save_cache(cache)
    except Exception:
        # Fail silently per requirements
        return


def getCourseEvaluation(courseCode: str) -> dict:
    """Return evaluation data for a course.

    Behavior:
    - If cached data exists, return it.
    - If no cache, start a background fetch and return empty dict immediately
      (lazy loading). This keeps the UI responsive and meets the requirement to
      fail silently when the external source is unreachable.

    Returned dict may contain `homeworkHours` (number) and `difficulty` (number).
    """
    try:
        key = _normalize(courseCode)
        cache = _load_cache()
        if key in cache:
            return cache[key]

        # Kick off background fetch and return empty result for now
        thread = threading.Thread(target=_background_fetch_and_cache, args=(courseCode,))
        thread.daemon = True
        thread.start()
        return {}
    except Exception:
        return {}
