from __future__ import annotations

from bc_portal.services.common import load_json


_PAYLOAD = load_json("study_spaces.json")

SERVICE_CARD = {
    "slug": "study-spaces",
    "name": "Study Spaces.",
    "kicker": "Libraries + Nearby Dining",
    "summary": (
        "Find a study location that matches your work style, check open hours, "
        "and see the best nearby coffee or meal option."
    ),
    "status": "Under construction",
    "cta": "Open study spaces desk",
    "metric_label": "Spaces indexed",
    "metric_value": str(len(_PAYLOAD["spaces"])),
}

FORM_FIELDS = [
    {
        "name": "study_style",
        "label": "Preferred study style",
        "type": "select",
        "options": ["Quiet focus", "Group collaboration", "Bright reading room"],
        "default": "Quiet focus",
    },
    {
        "name": "day",
        "label": "Day of visit",
        "type": "select",
        "options": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"],
        "default": "Tuesday",
    },
    {
        "name": "needs_outlets",
        "label": "Need reliable outlet access",
        "type": "checkbox",
        "default": True,
    },
]

BUILDER_CHALLENGE = {
    "headline": "Group Challenge: make recommendations feel campus-accurate",
    "description": (
        "Recommendations currently work, but there is no live crowding signal or "
        "closing-time warning. Add one realistic improvement that helps students "
        "trust the recommendation."
    ),
    "files": [
        "bc_portal/services/study_spaces.py",
        "bc_portal/data/study_spaces.json",
        "bc_portal/templates/service.html",
        "tests/test_portal.py",
    ],
    "prompt": (
        "Inspect the Study Spaces recommendation flow and data file, then propose "
        "one small service improvement that makes the result more useful for "
        "students. Before editing files, ask me to confirm the tradeoff; after I "
        "approve, run tests and summarize what changed."
    ),
    "stretch_goal": (
        "Add a closing-soon warning, a smarter fallback when the top space is "
        "crowded, or a nearby dining comparison. Add one validation test and keep "
        "the UI polished."
    ),
}

_STYLE_TO_VIBE = {
    "Quiet focus": "quiet",
    "Group collaboration": "collaborative",
    "Bright reading room": "sunny",
}


def _score_space(space: dict, vibe: str, needs_outlets: bool) -> int:
    score = 0
    if space["vibe"] == vibe:
        score += 3
    if needs_outlets and space["has_outlets"]:
        score += 2
    if space["crowd_level"] != "High":
        score += 1
    return score


def build_response(form_state: dict) -> dict:
    vibe = _STYLE_TO_VIBE[form_state["study_style"]]
    day = form_state["day"]
    ranked_spaces = sorted(
        _PAYLOAD["spaces"],
        key=lambda space: _score_space(space, vibe, form_state["needs_outlets"]),
        reverse=True,
    )
    top_space = ranked_spaces[0]
    top_hours = top_space["hours"].get(day, "Hours unavailable")

    return {
        "eyebrow": f"{top_space['zone']} | {form_state['study_style']}",
        "headline": f"Top recommendation: {top_space['name']}",
        "summary": (
            f"{top_space['name']} matches a {vibe} study style and is open {top_hours} "
            f"on {day}. Nearby food option: {top_space['nearby_dining']}."
        ),
        "metrics": [
            {"label": "Crowd level", "value": top_space["crowd_level"]},
            {"label": "Open hours", "value": top_hours},
            {"label": "Nearby dining", "value": top_space["nearby_dining"]},
        ],
        "primary_items": [
            top_space["description"],
            f"Best features: {', '.join(top_space['features'])}.",
            "Arrive 15 minutes early if you need your preferred seat or whiteboard space.",
        ],
        "secondary_title": "Backup options",
        "secondary_items": [
            f"{space['name']} | {space['zone']} | {space['hours'].get(day, 'Hours unavailable')}"
            for space in ranked_spaces[1:3]
        ],
        "status_note": (
            "Under construction: crowd level is currently a static mock field and "
            "does not update by time of day."
        ),
    }
