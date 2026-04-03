from __future__ import annotations

from bc_portal.services.common import load_json


_PAYLOAD = load_json("academic_advising.json")

SERVICE_CARD = {
    "slug": "academic-advising",
    "name": "Academic Advising",
    "kicker": "Degree Planning + Advisor Prep",
    "summary": (
        "Turn your current course load, academic priorities, and available study "
        "time into a weekly advising plan you can actually use."
    ),
    "status": "Under construction",
    "cta": "Open advising desk",
    "metric_label": "Advisors online",
    "metric_value": "4",
}

FORM_FIELDS = [
    {
        "name": "student_name",
        "label": "Student profile",
        "type": "select",
        "options": [student["name"] for student in _PAYLOAD["students"]],
        "default": _PAYLOAD["students"][0]["name"],
    },
    {
        "name": "priority",
        "label": "Top advising priority",
        "type": "select",
        "options": [
            "Balance my course load",
            "Prepare for midterms",
            "Plan a major/minor conversation",
            "Find academic support resources",
        ],
        "default": "Prepare for midterms",
    },
    {
        "name": "weekly_hours",
        "label": "Hours available this week",
        "type": "number",
        "default": 8,
        "min": 2,
        "max": 24,
    },
    {
        "name": "include_career_note",
        "label": "Include a career-center follow-up",
        "type": "checkbox",
        "default": True,
    },
]

BUILDER_CHALLENGE = {
    "headline": "Group Challenge: make advising feel personalized",
    "description": (
        "The current plan builder is useful, but it does not rank deadlines by "
        "risk or suggest a concrete advisor meeting next step. Add one meaningful "
        "upgrade without turning the flow into a giant form."
    ),
    "files": [
        "bc_portal/services/academic_advising.py",
        "bc_portal/data/academic_advising.json",
        "bc_portal/templates/service.html",
        "tests/test_portal.py",
    ],
    "prompt": (
        "Inspect the Academic Advising service and template, then propose one "
        "small feature that makes the advising plan more personalized. Implement "
        "the smallest useful version and add one test."
    ),
    "stretch_goal": (
        "Add an advisor-ready email draft or a deadline-risk score so the output "
        "feels closer to an actual advising workflow. Add one validation test and "
        "keep the UI polished."
    ),
}


def _find_student(student_name: str) -> dict:
    return next(
        student for student in _PAYLOAD["students"] if student["name"] == student_name
    )


def build_response(form_state: dict) -> dict:
    student = _find_student(form_state["student_name"])
    weekly_hours = max(int(form_state["weekly_hours"]), len(student["courses"]))
    hours_per_course = max(1, weekly_hours // len(student["courses"]))

    action_items = [
        f"Reserve {hours_per_course} focused hour(s) for {course['code']}: {course['next_step']}"
        for course in student["courses"]
    ]
    action_items.append(
        f"Bring one question about '{form_state['priority']}' to your next meeting with {student['advisor']}."
    )
    if form_state["include_career_note"]:
        action_items.append(student["career_note"])

    return {
        "eyebrow": f"{student['class_year']} | {student['school']}",
        "headline": f"{student['name']}'s advising plan",
        "summary": (
            f"{student['name']} is currently enrolled in {len(student['courses'])} courses and "
            f"wants to prioritize {form_state['priority'].lower()}. This draft plan keeps the "
            f"week structured while leaving room for one advisor follow-up."
        ),
        "metrics": [
            {"label": "Weekly study hours", "value": str(weekly_hours)},
            {"label": "Active courses", "value": str(len(student["courses"]))},
            {"label": "Advisor", "value": student["advisor"]},
        ],
        "primary_items": action_items,
        "secondary_title": "Campus resources to use this week",
        "secondary_items": student["support_resources"],
        "status_note": (
            "Under construction: this service does not yet rank deadline risk or "
            "generate an advisor email draft."
        ),
    }
