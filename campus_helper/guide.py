import json
from pathlib import Path

import yaml


REPO_ROOT = Path(__file__).resolve().parents[1]
GUIDE_CONTENT_PATH = REPO_ROOT / "campus_helper" / "guide_content" / "student_self_paced_guide.yaml"
GUIDE_PROGRESS_PATH = REPO_ROOT / ".student_guide_progress.json"

REQUIRED_MODULE_FIELDS = {
    "id",
    "title",
    "track",
    "section",
    "estimated_time",
    "prerequisites",
    "learning_objectives",
    "artifact_to_complete",
    "validation_step",
    "milestone_label",
    "steps",
    "checkpoints",
}

REQUIRED_STEP_FIELDS = {
    "action",
    "why_it_matters",
    "exact_prompt",
    "expected_result",
    "troubleshooting_note",
    "screenshot_ref",
}

REQUIRED_CHECKPOINT_FIELDS = {
    "student_input",
    "what_to_verify",
    "success_criteria",
    "stretch_option",
}


def load_guide_content(path: Path | None = None) -> dict:
    content_path = path or GUIDE_CONTENT_PATH
    with content_path.open() as handle:
        data = yaml.safe_load(handle)
    validate_guide_content(data)
    return data


def validate_guide_content(data: dict) -> None:
    if not isinstance(data, dict):
        raise ValueError("Guide content must be a mapping.")

    for key in ("title", "summary", "navigation", "modules", "resources"):
        if key not in data:
            raise ValueError(f"Guide content is missing '{key}'.")

    if not isinstance(data["modules"], list) or not data["modules"]:
        raise ValueError("Guide content must define at least one module.")

    for module in data["modules"]:
        missing = REQUIRED_MODULE_FIELDS - module.keys()
        if missing:
            missing_str = ", ".join(sorted(missing))
            raise ValueError(f"Module '{module.get('id', 'unknown')}' is missing: {missing_str}.")
        for step in module["steps"]:
            step_missing = REQUIRED_STEP_FIELDS - step.keys()
            if step_missing:
                missing_str = ", ".join(sorted(step_missing))
                raise ValueError(
                    f"Module '{module['id']}' has a step missing: {missing_str}."
                )
        for checkpoint in module["checkpoints"]:
            checkpoint_missing = REQUIRED_CHECKPOINT_FIELDS - checkpoint.keys()
            if checkpoint_missing:
                missing_str = ", ".join(sorted(checkpoint_missing))
                raise ValueError(
                    f"Module '{module['id']}' has a checkpoint missing: {missing_str}."
                )


def load_progress(path: Path | None = None) -> dict[str, str]:
    progress_path = path or GUIDE_PROGRESS_PATH
    if not progress_path.exists():
        return {}
    with progress_path.open() as handle:
        payload = json.load(handle)
    if not isinstance(payload, dict):
        return {}
    return {str(key): str(value) for key, value in payload.items()}


def save_progress(progress: dict[str, str], path: Path | None = None) -> None:
    progress_path = path or GUIDE_PROGRESS_PATH
    with progress_path.open("w") as handle:
        json.dump(progress, handle, indent=2, sort_keys=True)


def modules_for_section(data: dict, section_id: str) -> list[dict]:
    return [module for module in data["modules"] if module["section"] == section_id]


def resources_for_category(data: dict, category: str) -> list[dict]:
    return [resource for resource in data["resources"] if resource["category"] == category]


def completion_summary(data: dict, progress: dict[str, str]) -> tuple[int, int]:
    total = len(data["modules"])
    completed = sum(1 for module in data["modules"] if progress.get(module["id"]) == "Completed")
    return completed, total


def render_guide_markdown(data: dict) -> str:
    lines = [
        f"# {data['title']}",
        "",
        data["summary"],
        "",
        "## Navigation",
        "",
    ]

    for nav_item in data["navigation"]:
        lines.append(f"- **{nav_item['title']}**: {nav_item['description']}")

    for module in data["modules"]:
        lines.extend(
            [
                "",
                f"## {module['title']}",
                "",
                f"- Track: {module['track']}",
                f"- Section: {module['section']}",
                f"- Estimated time: {module['estimated_time']}",
                f"- Prerequisites: {', '.join(module['prerequisites']) or 'None'}",
                f"- Artifact to complete: {module['artifact_to_complete']}",
                f"- Validation step: {module['validation_step']}",
                f"- Milestone: {module['milestone_label']}",
                "",
                "### Learning objectives",
            ]
        )
        for objective in module["learning_objectives"]:
            lines.append(f"- {objective}")

        lines.append("")
        lines.append("### Steps")
        for index, step in enumerate(module["steps"], start=1):
            lines.extend(
                [
                    "",
                    f"#### Step {index}",
                    "",
                    f"**Action**: {step['action']}",
                    "",
                    f"**Why it matters**: {step['why_it_matters']}",
                    "",
                    "**Exact prompt**:",
                    "",
                    "```text",
                    step["exact_prompt"],
                    "```",
                    "",
                    f"**Expected result**: {step['expected_result']}",
                    "",
                    f"**Troubleshooting note**: {step['troubleshooting_note']}",
                    "",
                    f"**Screenshot reference**: {step['screenshot_ref']}",
                ]
            )

        lines.append("")
        lines.append("### Checkpoints")
        for checkpoint in module["checkpoints"]:
            lines.extend(
                [
                    "",
                    f"- Student input: {checkpoint['student_input']}",
                    f"- Verify: {checkpoint['what_to_verify']}",
                    f"- Success criteria: {checkpoint['success_criteria']}",
                    f"- Stretch option: {checkpoint['stretch_option']}",
                ]
            )

    if data["resources"]:
        lines.extend(["", "## Resources"])
        for resource in data["resources"]:
            lines.extend(
                [
                    "",
                    f"### {resource['title']}",
                    "",
                    f"- Category: {resource['category']}",
                    f"- Audience: {resource['audience']}",
                ]
            )
            for field_name in (
                "template",
                "example_output",
                "glossary_entry",
                "faq",
                "internal_only_note",
            ):
                field_value = resource.get(field_name)
                if field_value:
                    lines.extend(["", field_value])

    return "\n".join(lines).strip() + "\n"
