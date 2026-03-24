from campus_helper.skills.base import BaseSkill


class StudySpotsSkill(BaseSkill):
    skill_id = "study_spots"
    name = "Study Spot Recommender"
    description = "Matches a student preference to mock campus study spaces."
    next_prompt_hint = "Ask Codex to add filters for late-night spots or group-friendly spaces."
    input_fields = [
        {
            "key": "preferred_vibe",
            "label": "Preferred vibe",
            "type": "select",
            "options": ["quiet", "collaborative", "sunny"],
            "default": "quiet",
        },
        {
            "key": "day",
            "label": "Day to check",
            "type": "select",
            "options": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"],
            "default": "Tuesday",
        },
        {
            "key": "need_whiteboard",
            "label": "Need a whiteboard",
            "type": "checkbox",
            "default": True,
        },
    ]

    def run(self, inputs: dict, services: dict) -> str:
        study_space_service = services["study_spaces"]
        library_service = services["library_hours"]

        candidates = study_space_service.search(
            vibe=inputs["preferred_vibe"],
            need_whiteboard=inputs["need_whiteboard"],
        )

        if not candidates:
            return "## No matches found\nTry relaxing one filter and run the skill again."

        lines = []
        for spot in candidates[:3]:
            hours = None
            if spot.get("hours_key"):
                hours = library_service.get_hours(spot["hours_key"], inputs["day"])

            # TODO(workshop): keep the library-hours service contract aligned with this consumer.
            open_time = hours.get("open_time", "unavailable") if hours else "not listed"
            close_time = hours.get("close_time", "") if hours else ""
            hours_text = (
                f"{open_time} to {close_time}".strip()
                if hours
                else "Ask a teammate to add hours support."
            )

            features = ", ".join(spot["features"])
            lines.append(
                f"- **{spot['name']}** ({spot['zone']}): {spot['summary']} "
                f"Features: {features}. Hours on {inputs['day']}: {hours_text}."
            )

        joined = "\n".join(lines)
        return f"""
## Recommended study spots

Based on a **{inputs["preferred_vibe"]}** vibe, here are the best matches:

{joined}

### Suggested next Codex prompt
“Inspect the study spot service and improve how hours are shown in the UI.”
""".strip()
