# Campus Helper Agent Workshop

This repository is a complete starter project for a 50-minute hands-on workshop on AI-assisted coding with Codex.

Students all begin from the same codebase, create their own branch, and improve a small but realistic app called **Campus Helper Agent**. The app runs locally, uses mock JSON data, and is intentionally scaffolded so teams need to inspect the repo, iterate with Codex, and make changes across multiple files.

## What the app does

The starter app can help with student-oriented workflows like:

- generating study plans
- recommending study spots
- drafting club event blurbs
- looking up campus info from local mock data
- generating digest-style reminders

## Tech stack

- Python 3.10+
- Streamlit for the local UI
- Standard-library JSON-backed services
- Standard-library `unittest` for lightweight validation

This stack keeps setup light, avoids frontend build tooling, and lets students focus on architecture and AI-assisted iteration.

## Quick start

1. Create and activate a virtual environment:

   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Run the app:

   ```bash
   streamlit run app.py
   ```

4. Run the validation tests:

   ```bash
   python3 -m unittest discover -s tests
   ```

## Self-paced guide app

This repo now includes a separate self-paced learning guide for students who want
to keep practicing after the live workshop.

Run the guide app:

```bash
streamlit run guide_app.py
```

Export the same guide content to Markdown:

```bash
python3 scripts/export_guide.py
```

The guide is backed by a structured YAML source at
`campus_helper/guide_content/student_self_paced_guide.yaml`, so the app and the
shareable Markdown export stay in sync.

## Recommended workshop flow

1. Clone the repo.
2. Create a team branch.
3. Run the app and inspect the current behavior.
4. Use `WORKSHOP_CHALLENGES.md` to progress through the guided tasks.
5. Use Codex iteratively rather than trying to solve everything in one prompt.

## Folder structure

```text
.
├── app.py
├── campus_helper/
│   ├── automations/
│   ├── data/
│   ├── plugins/
│   ├── services/
│   ├── skills/
│   ├── runtime.py
│   └── workshop_registry.py
├── examples/
├── tests/
├── README.md
└── WORKSHOP_CHALLENGES.md
```

## Architecture overview

### Skills

Skills live in [`campus_helper/skills`](./campus_helper/skills). They are the main reusable capabilities the app can run.

Current examples:

- `StudyPlanSkill`
- `StudySpotsSkill`
- one additional skill that is implemented but not currently loading correctly

Students can add a new skill by:

- creating a new file in `skills/`
- following the existing class pattern
- registering it in `campus_helper/workshop_registry.py`

### Plugins

Plugins live in [`campus_helper/plugins`](./campus_helper/plugins). They modify the final output after a skill runs.

Current example:

- `CampusVoicePlugin`

Students can add another plugin without changing the core app runner. They only need to:

- create a new plugin class
- register it in `campus_helper/workshop_registry.py`

### Simplified MCP-style services

Services live in [`campus_helper/services`](./campus_helper/services). They mimic tool-connected services while staying fully local.

Current examples:

- study space lookup
- library hours lookup
- dining hall hours lookup

These services read local JSON files in [`campus_helper/data`](./campus_helper/data) and are consumed by skills or automations.

### Automations

Automations live in [`campus_helper/automations`](./campus_helper/automations). They simulate scheduled or trigger-based behavior with a button-driven workflow in the UI.

Current examples:

- `MorningDigestAutomation`
- `DeadlineNudgeAutomation` scaffold for extension

Students can add a new automation by following the pattern and registering it.

## Sample data and outputs

- Mock data: [`campus_helper/data`](./campus_helper/data)
- Sample outputs: [`examples`](./examples)
- Self-paced guide content: [`campus_helper/guide_content/student_self_paced_guide.yaml`](./campus_helper/guide_content/student_self_paced_guide.yaml)
- Markdown export target: [`exports/student_self_paced_guide.md`](./exports/student_self_paced_guide.md)

## Where students will work

Look for `TODO(workshop)` comments in:

- [`campus_helper/workshop_registry.py`](./campus_helper/workshop_registry.py)
- [`campus_helper/skills/study_spots.py`](./campus_helper/skills/study_spots.py)
- [`campus_helper/automations/deadline_nudge.py`](./campus_helper/automations/deadline_nudge.py)
