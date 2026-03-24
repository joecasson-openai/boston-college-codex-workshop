from campus_helper.skills.base import BaseSkill


class StudyPlanSkill(BaseSkill):
    skill_id = "study_plan"
    name = "Study Plan Builder"
    description = "Turns a course list and a goal into a short, realistic weekly plan."
    next_prompt_hint = "Ask Codex to add office-hours suggestions or exam prep logic."
    input_fields = [
        {
            "key": "student_name",
            "label": "Student name",
            "type": "text",
            "default": "Alex",
        },
        {
            "key": "courses",
            "label": "Courses",
            "type": "text",
            "default": "Biology, Calculus, History",
            "help": "Use comma-separated courses.",
        },
        {
            "key": "goal",
            "label": "Main goal this week",
            "type": "text",
            "default": "Stay ahead on readings and finish my bio lab write-up.",
        },
        {
            "key": "available_hours",
            "label": "Available study hours this week",
            "type": "number",
            "default": 8,
            "min_value": 1,
            "max_value": 25,
        },
        {
            "key": "constraints",
            "label": "Constraints or deadlines",
            "type": "textarea",
            "default": "Calculus quiz on Thursday, club meeting Wednesday night.",
        },
    ]

    def run(self, inputs: dict, services: dict) -> str:
        courses = [course.strip() for course in inputs["courses"].split(",") if course.strip()]
        hours = max(int(inputs["available_hours"]), len(courses))
        block_length = max(1, hours // max(len(courses), 1))

        course_lines = "\n".join(
            f"- **{course}**: reserve {block_length} focused hour(s) and finish one concrete task."
            for course in courses
        )

        return f"""
## Study Plan for {inputs["student_name"]}

### Weekly focus
{inputs["goal"]}

### Recommended blocks
{course_lines}

### Guardrails
- Protect one low-distraction block early in the week.
- Start the hardest assignment before the night it is due.
- End each session by writing the next tiny step in your notes.

### Constraints to keep in mind
{inputs["constraints"]}

### Suggested next Codex prompt
“Refactor this study-plan skill so it also creates a day-by-day schedule with meal breaks.”
""".strip()
