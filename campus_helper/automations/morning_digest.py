import json
from pathlib import Path

from campus_helper.automations.base import BaseAutomation


DATA_PATH = Path(__file__).resolve().parents[1] / "data" / "sample_assignments.json"


class MorningDigestAutomation(BaseAutomation):
    automation_id = "morning_digest"
    name = "Morning Digest"
    description = "Simulates a button-triggered daily digest for a student."
    input_fields = [
        {
            "key": "student_name",
            "label": "Student name",
            "type": "text",
            "default": "Alex",
        },
        {
            "key": "day",
            "label": "Digest day",
            "type": "select",
            "options": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"],
            "default": "Tuesday",
        },
        {
            "key": "dining_hall",
            "label": "Dining hall to include",
            "type": "select",
            "options": ["Hillside Cafe", "Stokes Hall Cafe"],
            "default": "Hillside Cafe",
        },
    ]

    def run(self, inputs: dict, services: dict) -> str:
        assignments = self._load_assignments()
        dining = services["dining"].get_hours(inputs["dining_hall"], inputs["day"])
        study_spot = services["study_spaces"].search(vibe="quiet", need_whiteboard=False)[0]

        tasks = assignments["students"].get(inputs["student_name"], assignments["students"]["Alex"])
        task_lines = "\n".join(
            f"- **{task['course']}**: {task['task']} (due {task['due']})"
            for task in tasks
        )

        return f"""
## Morning Digest for {inputs["student_name"]}

### Due soon
{task_lines}

### Smart place to work today
- {study_spot["name"]}: {study_spot["summary"]}

### Food checkpoint
- {inputs["dining_hall"]}: {dining["open_time"]} to {dining["close_time"]}
- Dining note: {dining["special"]}

### Suggested next Codex prompt
“Add a second automation that warns me when two deadlines land on the same day.”
""".strip()

    def _load_assignments(self) -> dict:
        with DATA_PATH.open() as handle:
            return json.load(handle)
