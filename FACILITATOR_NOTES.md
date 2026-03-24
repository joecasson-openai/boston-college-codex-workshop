# Facilitator Notes

## Intended learning outcomes

By the end of the workshop, students should be able to:

- inspect a multi-file codebase with Codex
- make small architectural changes instead of one-shot generation
- debug a registration problem
- debug a data-contract problem
- add a new feature using an existing pattern
- understand how merge conflicts happen around shared configuration files

## Seeded bugs

### Bug 1: registration/config mismatch

Location:

- `campus_helper/workshop_registry.py`

What is happening:

- A real skill exists in `campus_helper/skills/club_blurb.py`
- The registry points at the wrong module path, so the skill does not load

Expected student move:

- compare the registry entry with the real file path
- fix the import target
- rerun the app and verify the skill appears

### Bug 2: schema mismatch

Locations:

- `campus_helper/services/library_hours.py`
- `campus_helper/skills/study_spots.py`
- `campus_helper/data/library_hours.json`

What is happening:

- the service hands back raw hour keys like `opens_at` and `closes_at`
- the skill expects `open_time` and `close_time`
- result: the UI shows missing or incomplete hours

Expected student move:

- inspect the data shape
- decide whether to normalize in the service or adapt in the consumer
- verify the study spot output improves

## Suggested hints if students get stuck

### For the registration bug

- “Compare what the registry imports with the actual files on disk.”
- “What does the warning in the Streamlit sidebar tell you?”
- “Search for the class name and then search for the import string.”

### For the schema bug

- “Print or inspect the data returned by the service before it is rendered.”
- “Which keys exist in the JSON, and which keys does the skill read?”
- “Would you rather normalize data once in the service or handle it in every consumer?”

### For adding a new skill or plugin

- “Copy the smallest working example and change one thing at a time.”
- “Have Codex explain the pattern before asking it to write new code.”

## Merge-conflict discussion plan for the final 10 minutes

Designed hotspot:

- `campus_helper/workshop_registry.py`

Suggested facilitation flow:

1. Ask each team what they registered in the registry file.
2. Show how two branches editing the same list can conflict.
3. Explain how Git conflict markers work.
4. Discuss strategies:
   - smaller commits
   - pull and rebase or merge frequently
   - keep registry edits tidy and minimal
   - let Codex explain the conflict before fixing it

If you want to trigger a live example:

1. Have Team A add a skill registration.
2. Have Team B add a plugin registration on a nearby line.
3. Merge both into a demo branch and inspect the conflict.

## Suggested show-and-tell prompts

- “What bug did your team fix first, and how did Codex help?”
- “What new skill or plugin did you add?”
- “What file did you need to touch that you did not expect at first?”
- “If you had 20 more minutes, what would you extend next?”
- “What was the most useful kind of prompt you gave Codex?”
