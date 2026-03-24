# Campus Helper Student Self-Paced Codex Guide

A local-first learning guide for students who want to keep building with Codex after the live Campus Helper workshop. The guide keeps the strongest parts of the reference onboarding flow: sequenced actions, exact prompts, milestone unlocks, checkpoints, and an optional advanced path for saving and sharing work.


## Navigation

- **Start Here**: Learn what Codex is, what this repo contains, and how to resume work after class.
- **Core Path**: Follow the guided modules that reinforce the live workshop and get you back into flow quickly.
- **Practice Labs**: Debug the seeded issues step by step using the current Campus Helper codebase.
- **Build Your Own Project**: Extend the repo with a new student-facing capability or build a small project from a starter brief.
- **Troubleshooting**: Use targeted prompts, validation commands, and FAQs when you get stuck without an instructor nearby.
- **Optional Advanced Track**: Learn how to save, share, and optionally deploy your work without blocking the core learning path.

## Module 1: Start Here and Re-Enter the Workshop

- Track: core
- Section: start_here
- Estimated time: 10-15 minutes
- Prerequisites: Python 3.10+, Codex desktop app, Local copy of this repository
- Artifact to complete: The repo is open in Codex and the student can describe the purpose of the `skills`, `plugins`, `services`, and `automations` folders.
- Validation step: Open `README.md` and verify you can find the quick start, folder structure, and seeded bug descriptions.
- Milestone: Milestone unlocked: you can orient yourself in the repo without live help.

### Learning objectives
- Understand what the Campus Helper repo is meant to teach.
- Reopen the project in Codex without waiting for an instructor.
- Leave the module knowing where to look when you forget how the workshop is organized.

### Steps

#### Step 1

**Action**: Read the top-level README and compare the workshop flow to the folders in the repo.

**Why it matters**: Students often lose momentum after class because they forget where the architecture lives.

**Exact prompt**:

```text
Inspect this repository and explain, in plain language, what each of these folders is for:
`campus_helper/skills`, `campus_helper/plugins`, `campus_helper/services`,
`campus_helper/automations`, and `campus_helper/data`.

```

**Expected result**: A concise architecture explanation that matches the repo layout and workshop goals.

**Troubleshooting note**: If the explanation is vague, ask Codex to cite specific files in each folder.

**Screenshot reference**: README architecture overview and the repo file tree in Codex.

#### Step 2

**Action**: Re-state the workshop goals in your own words.

**Why it matters**: The guide should keep students anchored on outcomes, not just code edits.

**Exact prompt**:

```text
Summarize the purpose of this workshop repo for a student who missed the live intro.
Keep it to five bullets and mention the two seeded bugs.

```

**Expected result**: A five-bullet recap that includes the learning goals and the deliberate breakpoints.

**Troubleshooting note**: If the seeded bugs are missing, ask Codex to search for `TODO(workshop)` and identify the broken paths.

**Screenshot reference**: The Workshop Challenges document open beside the Codex response.

#### Step 3

**Action**: Set your personal restart point for the next time you open the repo.

**Why it matters**: Self-paced learners need an easy resume ritual after a long break.

**Exact prompt**:

```text
Based on this repository, tell me the three files I should reopen first when I come back later
and explain what question each file helps me answer.

```

**Expected result**: A short resume checklist, usually centered on `README.md`, `WORKSHOP_CHALLENGES.md`, and `campus_helper/workshop_registry.py`.

**Troubleshooting note**: If Codex suggests too many files, ask it to narrow the answer to the minimum three.

**Screenshot reference**: A local note or pinned Codex thread with the three-file resume checklist.

### Checkpoints

- Student input: Write one sentence describing what each major folder contributes to the app.
- Verify: Compare your sentences to the repo layout and the README architecture section.
- Success criteria: You can explain the repo without using generic phrases like "backend stuff" or "config stuff."
- Stretch option: Add one sentence about why `workshop_registry.py` is a merge-conflict hotspot.

- Student input: Save or pin a restart prompt for future sessions.
- Verify: Confirm your prompt mentions the files that should be re-opened first.
- Success criteria: You have a concrete restart instruction you can reuse after class.
- Stretch option: Ask Codex to turn your restart prompt into a reusable template.

## Module 2: Run Campus Helper Locally and Understand the App

- Track: core
- Section: core_path
- Estimated time: 15-20 minutes
- Prerequisites: Module 1 complete, Terminal access on the local machine
- Artifact to complete: The student can launch the main workshop app, describe each tab, and run the existing tests.
- Validation step: Run `python3 -m unittest discover -s tests` and confirm the tests pass before making code changes.
- Milestone: Milestone unlocked: you can boot the repo, inspect the UI, and validate the baseline.

### Learning objectives
- Run the current app locally.
- Understand what the main Streamlit app exposes today.
- Learn how to validate that the repo still works before making changes.

### Steps

#### Step 1

**Action**: Set up the local environment and install dependencies.

**Why it matters**: A repeatable setup path is the first blocker students hit when they return after class.

**Exact prompt**:

```text
Give me the exact terminal commands to create a virtual environment, install dependencies,
and run the Campus Helper Streamlit app for this repository.

```

**Expected result**: A short command list that includes creating `.venv`, installing `requirements.txt`, and running `streamlit run app.py`.

**Troubleshooting note**: If the commands span multiple lines, ask Codex to combine them into a copy-paste friendly sequence.

**Screenshot reference**: Terminal commands and the Streamlit app landing page.

#### Step 2

**Action**: Inspect the app tabs and the sidebar warnings.

**Why it matters**: The current app intentionally exposes both working paths and broken teaching moments.

**Exact prompt**:

```text
I have the app running. Explain what each tab is for and tell me what warnings or omissions
are intentionally part of the workshop.

```

**Expected result**: A tab-by-tab explanation and a note that optional components fail to load on purpose.

**Troubleshooting note**: If you do not see the warning area, refresh the app and inspect the sidebar again.

**Screenshot reference**: Main app overview tab and the sidebar component counts.

#### Step 3

**Action**: Validate the repo before changing code.

**Why it matters**: Students should build the habit of checking the baseline so they know whether they broke something new.

**Exact prompt**:

```text
Run the unit tests for this repository and summarize what they cover in plain language.

```

**Expected result**: Passing tests plus a simple description of what the existing tests assert.

**Troubleshooting note**: If a command fails because a dependency is missing, install the requirements first and rerun.

**Screenshot reference**: Terminal output for the passing unit test run.

### Checkpoints

- Student input: Describe what the Overview, Playground, Automations, and Services tabs each do.
- Verify: Compare your summary to the live app and `app.py`.
- Success criteria: You can tell a new student where to go for each kind of task without guessing.
- Stretch option: Identify one improvement you would make to the existing app navigation.

- Student input: Record the validation command you should run before editing code.
- Verify: Confirm it matches the test command in the README.
- Success criteria: You know how to re-check the baseline after future edits.
- Stretch option: Ask Codex to suggest one more low-cost validation command for this repo.

## Module 3: Debug the Broken Skill Registration

- Track: core
- Section: practice_labs
- Estimated time: 15-20 minutes
- Prerequisites: Module 2 complete
- Artifact to complete: The student can identify why the implemented club blurb skill does not appear and describe the fix.
- Validation step: Reopen the workshop app or inspect the warning output to confirm the bad class path is the root cause.
- Milestone: Milestone unlocked: you can trace a broken registration path through the repo.

### Learning objectives
- Trace a loading failure from the UI to the registry.
- Compare a declared class path to the actual file structure.
- Fix a small bug by inspecting the current code instead of guessing.

### Steps

#### Step 1

**Action**: Start from the symptom instead of the code.

**Why it matters**: Good debugging starts from what the app shows, not from random edits.

**Exact prompt**:

```text
The README says there is an implemented skill that is not loading correctly.
Inspect the repo and tell me which skill is missing from the app and why.

```

**Expected result**: Codex points to the `club_blurb` skill and the incorrect registry path.

**Troubleshooting note**: If the answer is uncertain, ask Codex to compare the registry import string to the actual file path on disk.

**Screenshot reference**: Sidebar warning message and the skill file list in `campus_helper/skills`.

#### Step 2

**Action**: Inspect the registry and the matching file side by side.

**Why it matters**: Students need practice comparing intended configuration with actual implementation.

**Exact prompt**:

```text
Compare `campus_helper/workshop_registry.py` with the files in `campus_helper/skills`.
Show me the exact mismatch that keeps the club blurb skill from loading.

```

**Expected result**: A direct comparison that shows the registry references `club_event_blurbs` while the real file is `club_blurb.py`.

**Troubleshooting note**: If Codex only says "the import is wrong," ask it to provide the exact before and after path strings.

**Screenshot reference**: Registry file and `club_blurb.py` visible at the same time.

#### Step 3

**Action**: Practice writing the fix before you apply it.

**Why it matters**: Self-paced learners benefit from articulating the intended change before they edit code.

**Exact prompt**:

```text
Do not edit the repo yet. Tell me the smallest code change needed to fix the missing skill
and how I would verify the fix afterward.

```

**Expected result**: A one-line registry change plus a verification step that the skill appears in the UI.

**Troubleshooting note**: If verification is vague, ask for both a UI check and a code-level check.

**Screenshot reference**: Your written fix plan or pinned Codex answer.

### Checkpoints

- Student input: Write the incorrect class path and the corrected class path.
- Verify: Confirm the strings match the current file name and class name in `club_blurb.py`.
- Success criteria: You can explain the bug as a configuration mismatch, not a logic bug.
- Stretch option: Ask Codex to explain why this type of issue is common in plugin or registry systems.

- Student input: Describe how you would verify the fix after editing.
- Verify: Confirm your verification includes reopening the app or refreshing the loaded skills.
- Success criteria: You can prove the bug is fixed, not just claim it.
- Stretch option: Add one test idea that would catch this earlier.

## Module 4: Debug the Service and Consumer Contract Mismatch

- Track: core
- Section: practice_labs
- Estimated time: 20-25 minutes
- Prerequisites: Module 2 complete, Familiarity with Module 3 debugging flow
- Artifact to complete: The student can explain why the study spots workflow shows missing hours and propose a clean fix.
- Validation step: Inspect `library_hours.json`, `library_hours.py`, and `study_spots.py` and identify which keys mismatch.
- Milestone: Milestone unlocked: you can debug a data contract across files.

### Learning objectives
- Trace data from JSON to a service to a skill consumer.
- Spot mismatched field names across boundaries.
- Decide whether the best fix belongs in the service or the consumer.

### Steps

#### Step 1

**Action**: Run the symptom path in the app.

**Why it matters**: The bug makes more sense when you connect the broken output to the underlying data contract.

**Exact prompt**:

```text
Inspect the study spots workflow in this repo and tell me why some hours show as unavailable or incomplete.
Trace the issue from the app output back to the code.

```

**Expected result**: Codex explains that the service returns `opens_at` and `closes_at` while the skill reads `open_time` and `close_time`.

**Troubleshooting note**: If the answer skips the JSON file, ask Codex to include the raw input shape as part of the trace.

**Screenshot reference**: Study spots output and the service/skill source files.

#### Step 2

**Action**: Compare the data boundary directly.

**Why it matters**: Students should learn to inspect the contract itself, not just the symptom.

**Exact prompt**:

```text
Compare the return shape from `campus_helper/services/library_hours.py` with what
`campus_helper/skills/study_spots.py` expects. Show me the exact field-name mismatch.

```

**Expected result**: A direct field-by-field comparison of the service output and the consumer expectation.

**Troubleshooting note**: If the explanation is abstract, ask Codex to show a sample dictionary for each side.

**Screenshot reference**: The relevant function in the service and the `open_time` lookup in the skill.

#### Step 3

**Action**: Evaluate the best fix location.

**Why it matters**: This is where students practice engineering judgment instead of only making code compile.

**Exact prompt**:

```text
Do not edit the code yet. Tell me whether the cleaner fix belongs in the service or in the consumer,
and justify the decision in three sentences.

```

**Expected result**: A recommendation, usually to normalize once in the service so future consumers do not repeat the adaptation.

**Troubleshooting note**: If Codex gives both options without choosing, ask it to commit to one default and explain why.

**Screenshot reference**: Your fix recommendation saved as a note next to the code.

### Checkpoints

- Student input: Write the raw JSON keys and the keys the skill expects.
- Verify: Confirm both sets of keys are copied exactly from the code or data file.
- Success criteria: You can state the mismatch without hand-waving.
- Stretch option: Draft a tiny test case that would assert the normalized output shape.

- Student input: Decide where you would normalize the data and why.
- Verify: Compare your answer to the service and skill responsibilities in the repo.
- Success criteria: Your reasoning addresses reuse, readability, and future maintenance.
- Stretch option: Ask Codex whether any other services in the repo should adopt the same shape.

## Module 5: Add One New Capability Using an Existing Pattern

- Track: core
- Section: core_path
- Estimated time: 20-30 minutes
- Prerequisites: Modules 2 through 4 complete
- Artifact to complete: A new capability plan and the first implementation pass for a small student-facing feature.
- Validation step: Pick one existing pattern to copy and state which file you will mirror before editing.
- Milestone: Milestone unlocked: you can extend the repo by following a known pattern.

### Learning objectives
- Extend the repo without rewriting its structure.
- Reuse an existing implementation pattern for a new student-facing capability.
- Practice asking Codex for bounded changes instead of one giant request.

### Steps

#### Step 1

**Action**: Choose a bounded feature idea.

**Why it matters**: Small, concrete features are easier to ship and easier to learn from than vague "make it better" requests.

**Exact prompt**:

```text
Based on the current Campus Helper repo, suggest three small new capabilities a student could add
in under 45 minutes. For each one, tell me which existing file is the best pattern to copy.

```

**Expected result**: Three realistic feature ideas with a recommended starting point from the current codebase.

**Troubleshooting note**: If the ideas are too ambitious, ask Codex to constrain them to one new file plus one registry update.

**Screenshot reference**: Feature options and the matched pattern files.

#### Step 2

**Action**: Turn the chosen idea into an implementation brief.

**Why it matters**: This builds the habit of making the task specific before editing code.

**Exact prompt**:

```text
I want to add this new capability: [describe your choice].
Turn it into a short implementation brief with the files to touch, the expected input fields,
and how I should verify it works.

```

**Expected result**: A brief with clear files, inputs, and a validation path.

**Troubleshooting note**: If the brief touches too many files, ask Codex to reduce it to a v1.

**Screenshot reference**: The implementation brief pinned in the Codex thread.

#### Step 3

**Action**: Create an exact edit prompt.

**Why it matters**: Students improve faster when they learn how to give Codex a bounded implementation task.

**Exact prompt**:

```text
Write the exact Codex prompt I should use to implement this feature in small, safe steps.
Make the prompt mention the pattern file it should follow.

```

**Expected result**: A ready-to-run implementation prompt that is narrow and specific.

**Troubleshooting note**: If the prompt is too broad, ask Codex to split it into "inspect first" and "then implement" phases.

**Screenshot reference**: The final implementation prompt ready to paste.

### Checkpoints

- Student input: Record the capability you chose and the existing file you will mimic.
- Verify: Confirm the pattern file already solves a similar problem in the repo.
- Success criteria: Your feature is scoped tightly enough for one study session.
- Stretch option: Define one follow-on enhancement you will deliberately postpone to v2.

- Student input: Save the implementation brief and prompt for reuse.
- Verify: Make sure they include both validation steps and file targets.
- Success criteria: You could come back tomorrow and continue without re-planning from scratch.
- Stretch option: Turn your implementation brief into a reusable template for future exercises.

## Module 6: Reflect, Consolidate, and Choose What to Try Next

- Track: core
- Section: core_path
- Estimated time: 10-15 minutes
- Prerequisites: Modules 1 through 5 complete
- Artifact to complete: A saved personal practice plan with one next task, one resume prompt, and one troubleshooting prompt.
- Validation step: Save your three prompts in a doc, note, or pinned thread and confirm they map to real repo actions.
- Milestone: Milestone unlocked: you have a personal after-class practice plan.

### Learning objectives
- Convert workshop actions into reusable learning habits.
- Identify the next best exercise instead of drifting after class.
- Create a personal after-class prompt set.

### Steps

#### Step 1

**Action**: Capture what you learned about the repo.

**Why it matters**: Reflection makes the next session faster and reduces repeated confusion.

**Exact prompt**:

```text
Summarize what I have learned from this repo so far in three sections:
architecture, debugging habits, and feature-building habits.

```

**Expected result**: A short, structured reflection anchored to this repository.

**Troubleshooting note**: If the answer sounds generic, ask Codex to tie each point to a specific file or bug.

**Screenshot reference**: Your saved reflection note.

#### Step 2

**Action**: Choose your next best exercise.

**Why it matters**: Students keep going longer when the next task is already chosen.

**Exact prompt**:

```text
Based on the current workshop repo and the exercises I have already completed,
recommend the single best next exercise for me and explain why it is the right next step.

```

**Expected result**: One recommended next exercise, not a long list.

**Troubleshooting note**: If Codex gives multiple options, ask it to rank them and pick one default.

**Screenshot reference**: The recommended next exercise with its rationale.

#### Step 3

**Action**: Save three reusable prompts.

**Why it matters**: Prompt reuse is part of self-paced learning, not just a convenience.

**Exact prompt**:

```text
Create three reusable prompts for this repo:
1) a restart prompt after a long break,
2) a debugging prompt for a broken feature,
3) a feature-planning prompt for a small extension.

```

**Expected result**: Three prompts you can save and reuse in future sessions.

**Troubleshooting note**: If the prompts are too abstract, ask Codex to include exact file references.

**Screenshot reference**: The three saved prompts in your notes or Codex thread.

### Checkpoints

- Student input: Write down your next exercise and why it comes next.
- Verify: Make sure the task builds on what you have already explored in the repo.
- Success criteria: You have a concrete follow-on task instead of a vague intention.
- Stretch option: Time-box the next session and define what "done" means.

- Student input: Save the restart, debugging, and feature-planning prompts.
- Verify: Confirm each prompt is specific to the Campus Helper repo.
- Success criteria: You can reopen the project later without re-inventing your prompts.
- Stretch option: Share the best prompt with a classmate and compare results.

## Module 7: Post-Class Extension - Add a New Skill

- Track: extension
- Section: build_your_own_project
- Estimated time: 30-45 minutes
- Prerequisites: Module 5 complete
- Artifact to complete: A new skill concept, file plan, registration plan, and verification checklist.
- Validation step: Identify the base skill class and the closest existing skill you will model.
- Milestone: Milestone unlocked: you can design a new skill path end to end.

### Learning objectives
- Create a new skill by following the existing class pattern.
- Register a new capability cleanly.
- Verify the skill appears in the UI and returns useful output.

### Steps

#### Step 1

**Action**: Pick a student-facing skill idea.

**Why it matters**: The skill track is the most direct way to turn a student use case into a visible extension.

**Exact prompt**:

```text
Suggest three new student-oriented skills that fit this repo.
For each one, tell me which existing skill is the best implementation pattern.

```

**Expected result**: Three skill ideas grounded in the current repo and a suggested starting file for each.

**Troubleshooting note**: If the ideas require new external APIs, ask for local-first versions instead.

**Screenshot reference**: Skill ideas and matched pattern files.

#### Step 2

**Action**: Plan the new skill in bounded terms.

**Why it matters**: A scoped skill brief prevents runaway prompts and fragile code changes.

**Exact prompt**:

```text
I want to add this new skill: [describe your idea].
Give me the input fields, output shape, files to edit, and a verification checklist.

```

**Expected result**: A concrete build plan covering the new skill file and the registry update.

**Troubleshooting note**: If the plan adds too many responsibilities, ask Codex to cut the feature to a minimal v1.

**Screenshot reference**: Skill brief with inputs and expected output.

#### Step 3

**Action**: Prepare a safe implementation prompt.

**Why it matters**: Students learn better when they ask for a small implementation slice tied to an existing pattern.

**Exact prompt**:

```text
Write the exact implementation prompt I should use to add this skill by following the style of
`campus_helper/skills/study_plan.py` or another closer pattern if appropriate.

```

**Expected result**: A single prompt that tells Codex what to inspect, what to create, and how to verify success.

**Troubleshooting note**: If the prompt does not mention the registry update, ask Codex to include it explicitly.

**Screenshot reference**: Final skill implementation prompt.

### Checkpoints

- Student input: Name your skill and list the user input fields it needs.
- Verify: Compare the fields to similar skills already in the repo.
- Success criteria: The input list is small, practical, and clearly tied to the output.
- Stretch option: Add one optional field that improves the output without making the skill hard to use.

- Student input: Write how you will verify the skill after implementation.
- Verify: Confirm the plan includes a UI check and one example run.
- Success criteria: You can tell whether the skill works without guesswork.
- Stretch option: Add a unit test idea for the new skill output.

## Module 8: Post-Class Extension - Add a New Plugin

- Track: extension
- Section: build_your_own_project
- Estimated time: 25-35 minutes
- Prerequisites: Module 5 complete
- Artifact to complete: A plugin idea, a short implementation brief, and a verification plan.
- Validation step: Identify the current plugin and explain what problem plugins solve in this app.
- Milestone: Milestone unlocked: you can add output transformations without touching core logic.

### Learning objectives
- Understand the plugin boundary in this repo.
- Add a transformation layer without changing core skill logic.
- Verify the plugin appears as an optional output enhancer.

### Steps

#### Step 1

**Action**: Inspect the current plugin boundary.

**Why it matters**: Plugins are intentionally lighter weight than new skills, and students should know when to choose them.

**Exact prompt**:

```text
Explain how plugins work in this repository and when I should add a plugin instead of a new skill.
Use the current plugin implementation as the example.

```

**Expected result**: A simple explanation tied to `CampusVoicePlugin` and the `apply_plugins` flow in `app.py`.

**Troubleshooting note**: If the answer does not mention the app runner, ask for the exact place where plugins are applied.

**Screenshot reference**: Plugin file and plugin application flow in `app.py`.

#### Step 2

**Action**: Choose a plugin transformation.

**Why it matters**: Good plugin ideas clearly modify presentation, tone, or structure without changing the underlying task.

**Exact prompt**:

```text
Suggest three plugin ideas for this repo that would transform output without changing the core skill logic.
Rank them by ease of implementation for a student.

```

**Expected result**: Three plugin ideas with a recommended easiest-first option.

**Troubleshooting note**: If Codex proposes logic-heavy ideas, remind it that plugins should only decorate or transform output.

**Screenshot reference**: Ranked plugin idea list.

#### Step 3

**Action**: Turn the chosen plugin into an implementation prompt.

**Why it matters**: Students should be able to execute the extension in one focused session.

**Exact prompt**:

```text
I want to build this plugin: [describe your choice].
Write the exact prompt I should use to add the plugin, register it, and verify it in the app.

```

**Expected result**: A concrete prompt covering the new plugin file, registry entry, and a sample run.

**Troubleshooting note**: If verification is missing, ask for the exact skill and plugin combination to demo.

**Screenshot reference**: Final plugin implementation prompt.

### Checkpoints

- Student input: Explain why your chosen feature should be a plugin instead of a skill.
- Verify: Compare your explanation to the current plugin behavior and app flow.
- Success criteria: Your plugin changes output format or presentation, not core data gathering logic.
- Stretch option: Design one second plugin that could stack with the first.

- Student input: Save one example input and expected transformed output.
- Verify: Check that the example demonstrates the plugin visibly.
- Success criteria: A classmate could tell the plugin worked just by looking at the output.
- Stretch option: Ask Codex how to make the plugin reusable across more than one skill.

## Module 9: Post-Class Extension - Finish or Improve an Automation

- Track: extension
- Section: build_your_own_project
- Estimated time: 25-40 minutes
- Prerequisites: Module 5 complete
- Artifact to complete: A plan for either finishing `DeadlineNudgeAutomation` or improving another automation path.
- Validation step: Identify what the unfinished automation currently does and what data source it should read next.
- Milestone: Milestone unlocked: you can reason about a local automation flow from input to output.

### Learning objectives
- Understand the local automation pattern in the repo.
- Use existing data to complete a scaffold or improve automation output.
- Verify automation behavior without a real scheduler.

### Steps

#### Step 1

**Action**: Compare the finished automation to the unfinished scaffold.

**Why it matters**: The best way to finish a scaffold is usually to copy the shape of a working example.

**Exact prompt**:

```text
Compare `campus_helper/automations/morning_digest.py` to
`campus_helper/automations/deadline_nudge.py`.
Tell me what is missing from the unfinished automation.

```

**Expected result**: A gap analysis covering missing logic, data use, and registration.

**Troubleshooting note**: If Codex misses the registry step, ask it to include the changes needed for the automation to appear in the UI.

**Screenshot reference**: Both automation files visible side by side.

#### Step 2

**Action**: Plan the smallest useful automation completion.

**Why it matters**: Students should finish with a working v1, not an over-designed automation.

**Exact prompt**:

```text
Give me a minimal v1 plan to finish `DeadlineNudgeAutomation` using the local assignments data.
Include the output shape, files to edit, and how to validate the automation in the app.

```

**Expected result**: A concise plan that reads from `sample_assignments.json`, returns a useful message, and registers the automation.

**Troubleshooting note**: If the plan adds scheduling infrastructure, ask Codex to stay within the local button-triggered pattern.

**Screenshot reference**: A v1 automation brief saved in your notes.

#### Step 3

**Action**: Generate an implementation prompt.

**Why it matters**: Students should be able to hand the repo and the brief to Codex without ambiguity.

**Exact prompt**:

```text
Write the exact implementation prompt I should use to finish the automation by following the
`MorningDigestAutomation` pattern and keeping the behavior local-first.

```

**Expected result**: A small-scope prompt that names the pattern file, expected data source, and verification step.

**Troubleshooting note**: If the prompt is too broad, ask Codex to split planning, implementation, and verification into separate phases.

**Screenshot reference**: Final automation implementation prompt.

### Checkpoints

- Student input: Write the single most important behavior the automation should add.
- Verify: Compare it to what a student would actually need from a reminder or nudge workflow.
- Success criteria: The automation solves one clear problem and stays local-first.
- Stretch option: Add one optional improvement you will leave for later.

- Student input: Record the data file and registry update involved.
- Verify: Confirm both are real paths in the repo.
- Success criteria: You know which files control the behavior and visibility of the automation.
- Stretch option: Ask Codex how the automation could be tested with a small fixture.

## Module 10: Build Your Own Mini Project from a Starter Brief

- Track: extension
- Section: build_your_own_project
- Estimated time: 45-60 minutes
- Prerequisites: Modules 7, 8, or 9 complete
- Artifact to complete: A starter brief selection, a v1 project plan, and a reusable execution prompt.
- Validation step: Pick one starter brief and reduce it to a single-session v1 before implementation.
- Milestone: Milestone unlocked: you can turn a project idea into a bounded Codex build.

### Learning objectives
- Combine what you learned into an independent but still bounded project.
- Use project briefs and checkpoints to keep Codex work structured.
- Practice choosing a v1 and deferring extras.

### Steps

#### Step 1

**Action**: Pick one starter brief.

**Why it matters**: Starter briefs keep independent work from becoming too open-ended.

**Exact prompt**:

```text
Show me three mini-project ideas that build on the Campus Helper repo and can be completed in one study session.
Each idea should feel useful for students and stay local-first.

```

**Expected result**: Three bounded project ideas that extend the repo naturally.

**Troubleshooting note**: If the projects feel too big, ask Codex to cut them to a one-file or one-feature v1.

**Screenshot reference**: Mini-project options saved in your notes.

#### Step 2

**Action**: Turn the chosen brief into a v1 spec.

**Why it matters**: This is the point where students practice narrowing scope like an engineer.

**Exact prompt**:

```text
I chose this mini project: [describe your idea].
Convert it into a v1 spec with success criteria, files to edit, validation commands, and one thing to defer.

```

**Expected result**: A small spec with clear scope boundaries and validation steps.

**Troubleshooting note**: If Codex adds multiple optional extras, ask it to defer all but one future enhancement.

**Screenshot reference**: The v1 mini-project spec.

#### Step 3

**Action**: Create an implementation sequence.

**Why it matters**: Independent projects go better when the steps are sequenced instead of improvised.

**Exact prompt**:

```text
Break this mini project into 4 to 6 implementation steps that I can work through with Codex.
Each step should end with a small validation check.

```

**Expected result**: A stepwise build plan with checks after each phase.

**Troubleshooting note**: If the steps are too big, ask Codex to shrink them until each step changes one behavior at a time.

**Screenshot reference**: Stepwise implementation checklist.

### Checkpoints

- Student input: Write the v1 success criteria for your mini project.
- Verify: Confirm the criteria describe one usable outcome and one validation path.
- Success criteria: You can tell when the project is done without adding extra scope.
- Stretch option: Add a "v2 later" note to prevent yourself from over-building.

- Student input: Save the implementation sequence.
- Verify: Make sure each step ends with a validation action.
- Success criteria: You could hand the sequence to another student and they could follow it.
- Stretch option: Ask Codex to estimate the time for each step.

## Optional Advanced Track: Save and Share Your Work with Git and GitHub

- Track: advanced
- Section: optional_advanced_track
- Estimated time: 20-30 minutes
- Prerequisites: Module 2 complete
- Artifact to complete: A short Git/GitHub workflow plan with the commands or UI steps needed to save work safely.
- Validation step: Identify whether you are using local-only work, public GitHub, or an internal repo with instructor guidance.
- Milestone: Milestone unlocked: you know how to save and share work without relying on memory.

### Learning objectives
- Understand why version control helps after class.
- Learn a student-safe path for saving changes to GitHub.
- Keep source control optional so it never blocks the core path.

### Steps

#### Step 1

**Action**: Decide whether you need source control for your current stage.

**Why it matters**: The advanced track should feel helpful, not mandatory.

**Exact prompt**:

```text
Explain when a student working on this repo should start using Git and GitHub,
and when it is still reasonable to stay local-only.

```

**Expected result**: A balanced explanation that makes Git optional but useful.

**Troubleshooting note**: If the answer sounds prescriptive, ask Codex to separate "good next step" from "required now."

**Screenshot reference**: A simple save-and-share decision checklist.

#### Step 2

**Action**: Get a student-safe save flow.

**Why it matters**: Learners need a practical save path that works outside internal tooling.

**Exact prompt**:

```text
Give me a beginner-friendly Git and GitHub workflow for this repo using public GitHub or another student-safe option.
Keep it short and local-first.

```

**Expected result**: A short workflow for cloning, branching or committing, and pushing work safely.

**Troubleshooting note**: If internal org setup appears, ask Codex to replace it with public GitHub guidance.

**Screenshot reference**: GitHub repo page and the commit or push steps.

#### Step 3

**Action**: Separate mixed-audience notes.

**Why it matters**: Some learners may be internal, but external students should not be blocked by internal assumptions.

**Exact prompt**:

```text
Give me a mixed-audience appendix:
one note for external students using public GitHub,
and one clearly labeled internal-only note for internal learners using internal repos.

```

**Expected result**: Two separate notes with clear boundaries.

**Troubleshooting note**: If the internal note dominates the answer, ask Codex to keep the external flow as the default.

**Screenshot reference**: Mixed-audience save and share appendix.

### Checkpoints

- Student input: Choose your save path for now.
- Verify: Make sure it matches your access level and current goals.
- Success criteria: You have a concrete, student-safe plan to save work.
- Stretch option: Add a branch naming habit for future exercises.

- Student input: Save the short Git/GitHub workflow.
- Verify: Confirm it does not depend on internal-only access unless you clearly labeled that section.
- Success criteria: A classmate could follow the flow without extra context.
- Stretch option: Ask Codex to explain the workflow in plain language for first-time Git users.

## Optional Advanced Track: Share or Deploy a Student Project

- Track: advanced
- Section: optional_advanced_track
- Estimated time: 20-30 minutes
- Prerequisites: Advanced Git/GitHub track complete
- Artifact to complete: A share or deployment plan that matches the student's audience and access.
- Validation step: Choose whether you only need a demo video, a GitHub repo, or an actual hosted app.
- Milestone: Milestone unlocked: you can choose an appropriate sharing path without over-engineering.

### Learning objectives
- Learn how to share a finished student project responsibly.
- Keep the default guide local-first while still exposing the next level.
- Separate external-safe deployment options from internal-only tooling.

### Steps

#### Step 1

**Action**: Pick the lightest sharing mechanism that matches your goal.

**Why it matters**: Not every project needs hosting; students should choose the simplest path that works.

**Exact prompt**:

```text
For a student-built Streamlit project like this one, explain when I should
1) just share the repo,
2) record a demo video,
3) host the app publicly.

```

**Expected result**: A simple decision guide for sharing options.

**Troubleshooting note**: If the answer jumps straight to deployment, ask Codex to compare all three options first.

**Screenshot reference**: Sharing decision checklist.

#### Step 2

**Action**: Get an external-student-safe deployment option.

**Why it matters**: The default guide must work for students without internal OpenAI infrastructure.

**Exact prompt**:

```text
Recommend one beginner-friendly way an external student could share a small Streamlit project
after finishing this repo, and explain the minimum steps involved.

```

**Expected result**: One public-safe deployment or sharing recommendation with minimal setup.

**Troubleshooting note**: If the answer references internal hosting, ask for a public alternative instead.

**Screenshot reference**: Public-safe sharing or deployment plan.

#### Step 3

**Action**: Capture the internal-only note separately.

**Why it matters**: Mixed audiences need clear boundaries so the default path stays clean.

**Exact prompt**:

```text
Give me a clearly labeled internal-only note for learners who do have internal deployment access,
but keep it separate from the main student flow.

```

**Expected result**: A small internal-only appendix that does not affect the external default path.

**Troubleshooting note**: If the answer merges internal and external paths together, ask Codex to split them into separate headings.

**Screenshot reference**: Internal-only deployment note.

### Checkpoints

- Student input: Choose your sharing path for the project you built.
- Verify: Match the path to your real audience and time budget.
- Success criteria: You picked the lightest path that still lets others see the work.
- Stretch option: Add a one-sentence rationale you could use when presenting the project.

- Student input: Save the external-safe sharing note and the internal-only note separately.
- Verify: Confirm the external path stands alone without internal assumptions.
- Success criteria: The main guide remains student-safe by default.
- Stretch option: Ask Codex for a small checklist to run before sharing publicly.

## Resources

### Starter brief - Exam prep skill

- Category: starter_brief
- Audience: all

Goal: Add a new skill that turns a course name, exam date, and study hours into a lightweight prep checklist.
Constraints: Keep the feature local-first, use the existing skill pattern, and aim for one new file plus a registry update.
Validation: The skill appears in the app and produces a checklist for one sample student.


### Starter brief - Study session plugin

- Category: starter_brief
- Audience: all

Goal: Add a plugin that converts any skill output into a more action-oriented checklist for students.
Constraints: Do not change core skill logic. Follow the current plugin pattern.
Validation: Run an existing skill with and without the plugin and compare the output.


### Starter brief - Deadline automation

- Category: starter_brief
- Audience: all

Goal: Finish the `DeadlineNudgeAutomation` flow using the local assignments file.
Constraints: Keep the automation button-triggered and local-first.
Validation: The automation appears in the app and returns a useful reminder for one sample student.


### Example output - Study plan

- Category: example_output
- Audience: all

Reuse `examples/study_plan_example.md` as the baseline output shape when students are learning how a skill should feel.
It is especially useful in Modules 2, 5, and 7 when students need to compare their output to an existing example.


### Example output - Morning digest

- Category: example_output
- Audience: all

Reuse `examples/morning_digest_example.md` when students need to understand the structure of a finished automation output.
It provides a concrete standard for the "due soon", "smart place to work", and "food checkpoint" sections.


### Troubleshooting - Local setup

- Category: troubleshooting
- Audience: all

If the app does not run:
- confirm you activated the virtual environment,
- reinstall dependencies from `requirements.txt`,
- rerun `python3 -m unittest discover -s tests`,
- then ask Codex to inspect the error from the terminal output instead of guessing.


### Troubleshooting - Confusing Codex answer

- Category: troubleshooting
- Audience: all

If Codex gives a vague answer, ask for one of these upgrades:
- "cite the exact file and line region"
- "show me the before and after path"
- "give me the smallest possible fix"
- "turn that into a validation checklist"


### Troubleshooting - Overscoped prompt

- Category: troubleshooting
- Audience: all

If Codex proposes too much at once, shrink the ask:
- ask it to inspect before editing,
- ask for a v1 only,
- ask for a plan with one validation step per phase,
- ask it to name the pattern file it should follow.


### Glossary - Skill

- Category: glossary
- Audience: all

A skill is a reusable capability class in `campus_helper/skills`.
In this repo, skills take structured input fields and return student-facing markdown output.


### Glossary - Plugin

- Category: glossary
- Audience: all

A plugin transforms the final output after a skill runs.
Plugins in this repo should change presentation, tone, or structure, not core logic.


### Glossary - Service contract

- Category: glossary
- Audience: all

A service contract is the shape of data a service returns and a consumer expects.
Module 4 uses a deliberate mismatch to teach students how to debug that boundary.


### FAQ - What if I forget everything between sessions?

- Category: faq
- Audience: all

Reopen `README.md`, `WORKSHOP_CHALLENGES.md`, and `campus_helper/workshop_registry.py`.
Then run your saved restart prompt from Module 1 and ask Codex to summarize your next best step.


### FAQ - Do I need GitHub before I can keep learning?

- Category: faq
- Audience: all

No. The core path is intentionally local-first.
GitHub helps once you want better version history or an easier way to share the work with others.


### FAQ - Do I need deployment before I can show progress?

- Category: faq
- Audience: all

No. A repo link, screenshots, or a short demo video are all valid sharing paths.
Deployment belongs in the optional advanced track.


### Internal-only note - Internal repo and deployment variants

- Category: internal_note
- Audience: internal_only

If the learner is internal and has approved access to internal tooling, keep those notes in a clearly labeled appendix.
The external-safe path should remain the default everywhere else in the guide.
