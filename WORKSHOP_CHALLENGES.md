# Workshop Challenges

These challenges are designed for small teams working with Codex over roughly 35
minutes.

Each group should ship one small vertical slice on its own branch:

- a skill
- a plugin that transforms that skill's output
- an automation that runs the skill in a repeatable workflow

If there are more than three groups, reuse one of the challenge tracks below.
Multiple groups can choose the same track as long as each group pushes to its own
branch, such as `group-1`, `group-2`, or `group-3`.

## How to split work inside one group

Use one shared branch per group, then divide the feature implementation by file
ownership:

- **Skill owner** works in `campus_helper/skills`
- **Plugin owner** works in `campus_helper/plugins`
- **Automation owner** works in `campus_helper/automations`
- **Integrator** updates `campus_helper/workshop_registry.py`, runs tests, and
  checks the final app behavior

Recommended sequence:

1. Pick one challenge track below.
2. Ask Codex to inspect the closest existing pattern files.
3. Build the skill, plugin, and automation in parallel.
4. Have one person register the new classes in `workshop_registry.py`.
5. Run the app and `python3 -m unittest discover -s tests`.
6. Prepare a 1-minute demo of what your group built and what you had to steer
   Codex on.

## Challenge Track 1: Exam Prep Pack

Goal: help a student turn an upcoming exam into a short prep plan and a repeatable
reminder workflow.

Suggested build:

- **Skill**: create an `ExamPrepSkill` that takes course name, exam date, topics,
  and available hours, then returns a checklist or study plan.
- **Plugin**: create a plugin that converts the skill output into a tighter
  checklist, a motivational study format, or a "what to do today" summary.
- **Automation**: create an automation that runs the exam prep skill for a
  sample student and produces a "study nudge" output.

Good Codex prompts:

- "Inspect the existing skill, plugin, and automation patterns and tell us the
  smallest set of files to copy for an Exam Prep Pack."
- "Create a first-pass `ExamPrepSkill` that follows the `StudyPlanSkill` pattern,
  then summarize how to register and test it."
- "Create one plugin and one automation that use the new exam prep skill, but
  keep the implementation local-first and small enough for a classroom demo."

## Challenge Track 2: Club Event Promo Pack

Goal: help a club generate a short event blurb and turn it into a reusable event
announcement workflow.

Suggested build:

- **Skill**: use or improve the club blurb skill so it generates a cleaner event
  announcement for a selected club, audience, and tone.
- **Plugin**: create a plugin that transforms the blurb into a social caption,
  poster checklist, or "ready to share" format.
- **Automation**: create an automation that generates a weekly event promo digest
  or a reminder for one selected club.

Good Codex prompts:

- "Inspect why the club blurb skill is not appearing in the app, explain the
  issue, and make the smallest fix."
- "Create a plugin that turns club blurb output into a social-post draft without
  changing the underlying skill logic."
- "Create a lightweight event promo automation that follows the
  `MorningDigestAutomation` pattern and uses the club blurb skill's output style."

## Challenge Track 3: Study Day Planner Pack

Goal: help a student choose a study spot, understand open hours, and get a
repeatable daily study suggestion.

Suggested build:

- **Skill**: improve the study spot recommender or add a new planning skill that
  includes where to study and when to go.
- **Plugin**: create a plugin that converts the recommendation into a concise
  itinerary, checklist, or "next best move" summary.
- **Automation**: create an automation that produces a morning study suggestion
  by combining a recommended spot with one deadline or food checkpoint.

Good Codex prompts:

- "Trace why the study spot workflow shows unavailable hours, identify the exact
  service/consumer mismatch, and recommend the cleanest fix."
- "Create a plugin that turns the study spot recommendation into a concise
  itinerary with a clear next action."
- "Create a morning study suggestion automation by following the existing
  automation pattern and reusing local service data."

## Shared implementation checklist

Before your demo, make sure your group can show:

- the new or improved skill in the Playground tab
- the plugin applied to that skill's output
- the automation in the Automations tab
- one validation command or manual test you used
- one example of how you prompted Codex and then refined the result
