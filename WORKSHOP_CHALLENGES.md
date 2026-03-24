# Workshop Challenges

These challenges are designed for small teams working with Codex over roughly 35 minutes.

## Challenge 1: Add a new skill

Goal: add a new reusable capability in `campus_helper/skills`.

Suggested path:

1. Inspect the existing skill classes.
2. Notice that one implemented skill is not appearing in the app.
3. Fix the registration issue in `campus_helper/workshop_registry.py`.
4. Add your own new skill, such as:
   - exam prep checklist
   - office-hours question generator
   - weekend reset planner
5. Register your new skill and confirm it appears in the Streamlit UI.

Good Codex prompts:

- “Inspect the skill architecture and explain how to add a new skill.”
- “Fix the broken skill registration and add a new `ExamPrepSkill` following the existing pattern.”

## Challenge 2: Add a new plugin

Goal: create a plugin that visibly transforms output without changing core app logic.

Suggested plugin ideas:

- convert outputs into a checklist
- add a concise executive summary at the top
- add “next prompt ideas” tailored to the selected skill
- add a “student-friendly tone” layer

Expected files:

- a new file in `campus_helper/plugins`
- an entry in `campus_helper/workshop_registry.py`

Good Codex prompts:

- “Create a plugin that reformats skill output into a demo-friendly checklist.”
- “Show me how plugins are applied in this repo and add a new one.”

## Challenge 3: Connect or fix a tool-backed service

Goal: debug the visible data issue in the study spot workflow.

Suggested path:

1. Run the study spot skill.
2. Notice that some hours are not shown correctly.
3. Inspect:
   - `campus_helper/services/library_hours.py`
   - `campus_helper/skills/study_spots.py`
   - `campus_helper/data/library_hours.json`
4. Fix the contract mismatch so the hours display correctly.
5. If you finish early, extend the service or skill with another useful field.

Good Codex prompts:

- “Trace why the study spot skill is showing unavailable hours.”
- “Fix the schema mismatch between the library-hours service and its consumer.”

## Challenge 4: Add or repair an automation

Goal: extend the automation pattern using the provided scaffold.

Suggested path:

1. Inspect `MorningDigestAutomation`.
2. Open `campus_helper/automations/deadline_nudge.py`.
3. Finish the placeholder logic using local assignment data.
4. Register the automation in `campus_helper/workshop_registry.py`.
5. Confirm it appears and runs in the UI.

Possible automation ideas:

- deadline warning
- club meeting reminder
- “best next study block” suggestion
- Friday weekly wrap-up

Good Codex prompts:

- “Use the morning digest pattern to finish the deadline nudge automation.”
- “Register the new automation and make it visible in the app.”
