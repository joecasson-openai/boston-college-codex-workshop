# Heights Student Services Portal

A Boston College-inspired student services portal for a hands-on Codex workshop.

Students use the portal as if it were a real campus product, then work in small
groups to improve one under-construction service on their own branch. The goal is
to practice a practical Codex workflow: inspect the codebase, make a focused
implementation, validate the change, and explain the diff before pushing to
GitHub.

## What you are building

The portal has three student-facing service areas:

- **Academic Advising**
  Build better course planning, deadline prioritization, and advising next steps.
- **Campus Life**
  Improve club and event communication so announcements feel polished and
  ready to share.
- **Study Spaces**
  Improve study-space recommendations with hours, crowd context, and nearby
  food options.

Each service page includes a **Builder Challenge** panel with a starter prompt,
files to inspect, and a **Bonus Challenge** if your group finishes early. The
main service UI should feel like a real student portal; the challenge panel is
the workshop scaffolding.

## Before class: install Codex

Choose one Codex setup path before the workshop.

### Option 1: Codex app

Recommended on macOS and Windows if you want the full desktop workflow.

1. Download Codex from the [Codex app page](https://developers.openai.com/codex/app/).
2. Open Codex and sign in with your ChatGPT account.
3. Clone this repository locally.
4. In Codex, select this repo folder as your project.
5. Make sure **Local** mode is selected before asking Codex to inspect or edit
   files on your machine.

### Option 2: Codex IDE extension

Use this if you prefer to work inside VS Code, Cursor, or Windsurf.

1. Install the extension from the
   [Codex IDE page](https://developers.openai.com/codex/ide/).
2. Open this repository in your editor.
3. Open the Codex panel, sign in, and ask Codex to inspect the current project.

### Option 3: Codex CLI

Use this if you prefer terminal-first development or if you are on Linux.

```bash
npm i -g @openai/codex
codex
```

You can also install with Homebrew:

```bash
brew install codex
codex
```

More setup details are in the [Codex quickstart](https://developers.openai.com/codex/quickstart/).

## Before class: verify your local Python environment

The app runs locally with Flask and standard Python tests. Use Python 3.10+.

### macOS or Linux

```bash
git clone https://github.com/joecasson-openai/boston-college-codex-workshop.git
cd boston-college-codex-workshop

python3 -m venv .venv
source .venv/bin/activate
python3 -m pip install --upgrade pip
python3 -m pip install -r requirements.txt

python3 -c "import flask; print('Environment ready')"
python3 -m unittest discover -s tests
python3 app.py
```

### Windows PowerShell

```powershell
git clone https://github.com/joecasson-openai/boston-college-codex-workshop.git
cd boston-college-codex-workshop

py -m venv .venv
.\.venv\Scripts\Activate.ps1
py -m pip install --upgrade pip
py -m pip install -r requirements.txt

py -c "import flask; print('Environment ready')"
py -m unittest discover -s tests
py app.py
```

Then open `http://127.0.0.1:5001`.

If activation fails on Windows because PowerShell blocks scripts, run
`Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass`, activate the
virtual environment again, and continue.

## Workshop flow

1. Pull the latest `main` branch.
2. Create one branch for your group, such as `group-1-academic-advising`,
   `group-2-campus-life`, or `group-3-study-spaces`.
3. Run the portal and click through each service once before editing anything.
4. Pick your group’s service area and read the Builder Challenge panel.
5. Ask Codex to explain the route, service module, template, and test files that
   power that workflow.
6. Ask Codex for a small implementation plan, then make one focused change.
7. Run the tests, manually check the UI, and ask Codex to summarize the diff.
8. Commit and push your group branch to GitHub.

## Suggested team roles

Everyone works from the same repository, but each group pushes to its own
branch.

- **Service logic owner**: updates one module in `bc_portal/services`
- **UI owner**: improves `bc_portal/templates/service.html` and
  `bc_portal/static/styles.css`
- **Data and test owner**: updates one JSON file in `bc_portal/data` and adds or
  extends a test in `tests/test_portal.py`
- **Integrator**: runs the app, checks the final branch, and prepares the demo

If your group has fewer people, combine roles. If there are more than three
groups, multiple groups can choose the same service as long as they work on
separate branches.

## Suggested Codex prompts

Start with inspection before implementation:

```text
Inspect the Academic Advising route, service module, template, and tests. Explain
how a form submission turns into the response card, and identify one small,
high-value improvement our group could ship today. Do not edit files yet.
```

After the group confirms the plan, ask for a bounded implementation:

```text
Implement the smallest useful version of that improvement across the service,
template, and tests. Keep the UI polished, run validation, and summarize the
diff when you are done.
```

For review and debugging:

```text
Run the test suite, inspect any failing behavior in our service branch, and
recommend the smallest safe fix. Do not rewrite unrelated files.
```

## Project map

```text
.
├── app.py
├── bc_portal/
│   ├── __init__.py
│   ├── data/
│   ├── services/
│   ├── static/
│   └── templates/
├── tests/
└── README.md
```

Useful files by service:

- Academic Advising: `bc_portal/services/academic_advising.py`
- Campus Life: `bc_portal/services/campus_life.py`
- Study Spaces: `bc_portal/services/study_spaces.py`
- Shared page template: `bc_portal/templates/service.html`
- Shared styling: `bc_portal/static/styles.css`
- Validation tests: `tests/test_portal.py`

## Keep building after the workshop

- [Codex overview](https://developers.openai.com/codex/)
- [Codex for Students](https://developers.openai.com/community/students)
- [Codex for Open Source](https://openai.com/form/codex-for-oss/)
- [Codex Ambassadors](https://developers.openai.com/community/codex-ambassadors)
- [OpenAI Developers Community](https://developers.openai.com/community)
