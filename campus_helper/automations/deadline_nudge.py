from campus_helper.automations.base import BaseAutomation


class DeadlineNudgeAutomation(BaseAutomation):
    automation_id = "deadline_nudge"
    name = "Deadline Nudge"
    description = "A starter scaffold for Challenge 4."
    input_fields = [
        {
            "key": "student_name",
            "label": "Student name",
            "type": "text",
            "default": "Alex",
        }
    ]

    def run(self, inputs: dict, services: dict) -> str:
        # TODO(workshop): finish this automation so it checks local assignment data.
        # TODO(workshop): register it in campus_helper/workshop_registry.py.
        return "## Deadline Nudge\nThis automation is intentionally unfinished for the workshop."
