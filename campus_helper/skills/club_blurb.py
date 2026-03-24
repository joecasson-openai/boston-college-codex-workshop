import json
from pathlib import Path

from campus_helper.skills.base import BaseSkill


DATA_PATH = Path(__file__).resolve().parents[1] / "data" / "clubs.json"


class ClubEventBlurbSkill(BaseSkill):
    skill_id = "club_blurb"
    name = "Club Event Blurb Draft"
    description = "Drafts a short campus-club event blurb using local club metadata."
    next_prompt_hint = "Ask Codex to add multiple tone presets or social-post output."
    input_fields = [
        {
            "key": "club_name",
            "label": "Club name",
            "type": "select",
            "options": ["Coding Club", "Eco Collective", "Debate Society"],
            "default": "Coding Club",
        },
        {
            "key": "event_name",
            "label": "Event name",
            "type": "text",
            "default": "Build Night",
        },
        {
            "key": "audience",
            "label": "Audience",
            "type": "text",
            "default": "students who are curious about beginner-friendly AI projects",
        },
        {
            "key": "tone",
            "label": "Tone",
            "type": "select",
            "options": ["friendly", "energetic", "professional"],
            "default": "friendly",
        },
    ]

    def run(self, inputs: dict, services: dict) -> str:
        club_data = self._load_club_data()
        club = next(item for item in club_data if item["name"] == inputs["club_name"])

        tone_line = {
            "friendly": "Come by, meet new people, and leave with something useful.",
            "energetic": "Bring your laptop and your curiosity for a fast-moving session.",
            "professional": "Join us for a practical session focused on applied campus projects.",
        }[inputs["tone"]]

        return f"""
## Draft club blurb

**{inputs["event_name"]}** is hosted by **{club["name"]}**, a group focused on {club["mission"]}.
This event is designed for {inputs["audience"]}. {tone_line}

Why attend:
- Learn something concrete in under an hour
- Meet peers with similar interests
- Leave with a next step you can build on

Location idea: {club["default_location"]}
""".strip()

    def _load_club_data(self) -> list[dict]:
        with DATA_PATH.open() as handle:
            payload = json.load(handle)
        return payload["clubs"]
