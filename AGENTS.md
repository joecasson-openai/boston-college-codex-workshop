# AGENTS.md

## Project Goal

This repo is a hands-on Codex workshop project. The app should feel like a
realistic Boston College student services portal first, and a teaching scaffold
second.

Students work in groups on separate branches to improve one service area:
Academic Advising, Campus Life, or Study Spaces.

## Repo Map

- `app.py` - Flask entrypoint
- `bc_portal/__init__.py` - app factory and route wiring
- `bc_portal/services/` - service-specific business logic and challenge metadata
- `bc_portal/data/` - local JSON data backing each service
- `bc_portal/templates/` - shared Jinja layouts and service pages
- `bc_portal/static/styles.css` - shared UI styling
- `tests/test_portal.py` - request/response validation tests

## How To Run

```bash
python3 -m pip install -r requirements.txt
python3 -m unittest discover -s tests
python3 app.py
```

Use `py` instead of `python3` on Windows PowerShell if that is the configured
launcher.

## Working Rules

- Inspect the relevant route, service module, template, and test before editing.
- Keep each change small and scoped to one service workflow when possible.
- Preserve the BC-inspired visual style and keep UI output polished enough to
  demo live.
- Add or update at least one validation test when changing service behavior.
- Do not edit unrelated files or private instructor-only materials.
- Summarize what changed and how it was validated before finishing.
