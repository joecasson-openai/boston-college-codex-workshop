from __future__ import annotations

from bc_portal.services.common import load_json


_PAYLOAD = load_json("campus_life.json")

SERVICE_CARD = {
    "slug": "campus-life",
    "name": "Campus Life.",
    "kicker": "Clubs + Event Promotion",
    "summary": (
        "Draft event announcements and outreach plans for student organizations "
        "using local club and venue information."
    ),
    "status": "Under construction",
    "cta": "Open campus life desk",
    "metric_label": "Active orgs",
    "metric_value": str(len(_PAYLOAD["clubs"])),
}

FORM_FIELDS = [
    {
        "name": "club_name",
        "label": "Student organization",
        "type": "select",
        "options": [club["name"] for club in _PAYLOAD["clubs"]],
        "default": _PAYLOAD["clubs"][0]["name"],
    },
    {
        "name": "event_name",
        "label": "Event name",
        "type": "text",
        "default": "Build Night",
    },
    {
        "name": "audience",
        "label": "Target audience",
        "type": "text",
        "default": "students curious about hands-on AI projects",
    },
    {
        "name": "tone",
        "label": "Announcement tone",
        "type": "select",
        "options": ["Warm and welcoming", "High-energy", "Professional"],
        "default": "Warm and welcoming",
    },
]

BUILDER_CHALLENGE = {
    "headline": "Group Challenge: ship a stronger event promotion workflow",
    "description": (
        "The announcement generator works, but it does not yet create a channel-"
        "specific checklist or timing plan for publishing. Add one practical "
        "feature a student club would care about."
    ),
    "files": [
        "bc_portal/services/campus_life.py",
        "bc_portal/data/campus_life.json",
        "bc_portal/templates/service.html",
        "tests/test_portal.py",
    ],
    "prompt": (
        "Inspect the Campus Life workflow from form submission to announcement "
        "card. Improve one realistic part of the output or event-planning data, "
        "then validate the route with a test."
    ),
    "stretch_goal": (
        "Generate channel-specific announcement variants or a posting timeline "
        "that a student organization could use immediately. Add one validation "
        "test and keep the UI polished."
    ),
}


def _find_club(club_name: str) -> dict:
    return next(club for club in _PAYLOAD["clubs"] if club["name"] == club_name)


def _tone_line(tone: str) -> str:
    if tone == "High-energy":
        return "Bring a friend, jump into the activity, and leave with momentum."
    if tone == "Professional":
        return "Join us for a focused session with clear takeaways and follow-up resources."
    return "Come as you are, meet other students, and leave with a next step."


def build_response(form_state: dict) -> dict:
    club = _find_club(form_state["club_name"])
    tone_line = _tone_line(form_state["tone"])

    return {
        "eyebrow": f"{club['category']} | {club['default_venue']}",
        "headline": f"{form_state['event_name']} announcement draft",
        "summary": (
            f"{form_state['event_name']} is hosted by {club['name']}, a student "
            f"organization focused on {club['mission']}. This draft is written for "
            f"{form_state['audience']}."
        ),
        "metrics": [
            {"label": "Best venue", "value": club["default_venue"]},
            {"label": "Audience size", "value": club["expected_turnout"]},
            {"label": "Posting window", "value": club["recommended_post_day"]},
        ],
        "primary_items": [
            f"Announcement copy: {tone_line}",
            f"Highlight one hook: {club['signature_hook']}",
            f"Invite students to RSVP or stop by {club['default_venue']}.",
        ],
        "secondary_title": "Promotion checklist",
        "secondary_items": club["promotion_checklist"],
        "status_note": (
            "Under construction: this service does not yet generate platform-"
            "specific versions for email, Instagram, and campus bulletin posts."
        ),
    }
