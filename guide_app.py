from collections import defaultdict

import streamlit as st

from campus_helper.guide import (
    completion_summary,
    load_guide_content,
    load_progress,
    modules_for_section,
    resources_for_category,
    save_progress,
)


st.set_page_config(
    page_title="Campus Helper Self-Paced Guide",
    page_icon="🧭",
    layout="wide",
)

STATUS_OPTIONS = ["Not started", "In progress", "Completed"]
RESOURCE_CATEGORY_LABELS = {
    "starter_brief": "Starter Briefs",
    "example_output": "Example Outputs",
    "troubleshooting": "Troubleshooting",
    "glossary": "Glossary",
    "faq": "FAQ",
    "internal_note": "Internal-Only Notes",
}


def status_badge(status: str) -> str:
    if status == "Completed":
        return ":green-badge[Completed]"
    if status == "In progress":
        return ":orange-badge[In progress]"
    return ":gray-badge[Not started]"


def module_card(module: dict, progress: dict[str, str]) -> None:
    status = progress.get(module["id"], "Not started")
    st.markdown(f"### {module['title']}")
    left, right = st.columns([3, 1])
    with left:
        st.caption(
            f"{module['track'].title()} track | {module['estimated_time']} | "
            f"Milestone: {module['milestone_label']}"
        )
    with right:
        st.markdown(status_badge(status))

    st.write(module["artifact_to_complete"])
    st.markdown("**Prerequisites**")
    for prerequisite in module["prerequisites"]:
        st.markdown(f"- {prerequisite}")

    st.markdown("**Learning objectives**")
    for objective in module["learning_objectives"]:
        st.markdown(f"- {objective}")

    st.markdown("**Validation step**")
    st.info(module["validation_step"])

    for index, step in enumerate(module["steps"], start=1):
        with st.expander(f"Step {index}: {step['action']}", expanded=index == 1):
            st.markdown("**Why it matters**")
            st.write(step["why_it_matters"])
            st.markdown("**Exact prompt**")
            st.code(step["exact_prompt"], language="text")
            st.markdown("**Expected result**")
            st.write(step["expected_result"])
            st.markdown("**If you get stuck**")
            st.warning(step["troubleshooting_note"])
            st.caption(f"Suggested screenshot or artifact: {step['screenshot_ref']}")

    st.markdown("**Checkpoints**")
    for checkpoint in module["checkpoints"]:
        st.markdown(f"- Student input: {checkpoint['student_input']}")
        st.markdown(f"- Verify: {checkpoint['what_to_verify']}")
        st.markdown(f"- Success criteria: {checkpoint['success_criteria']}")
        st.markdown(f"- Stretch option: {checkpoint['stretch_option']}")

    selected_status = st.radio(
        "Progress",
        STATUS_OPTIONS,
        index=STATUS_OPTIONS.index(status),
        key=f"status-{module['id']}",
        horizontal=True,
    )
    if selected_status != status:
        progress[module["id"]] = selected_status
        save_progress(progress)

    st.divider()


def render_section(title: str, description: str, modules: list[dict], progress: dict[str, str]) -> None:
    st.title(title)
    st.caption(description)
    if not modules:
        st.info("No modules live in this section yet.")
        return
    for module in modules:
        module_card(module, progress)


def render_resources(data: dict) -> None:
    st.title("Troubleshooting and Resources")
    grouped = defaultdict(list)
    for resource in data["resources"]:
        grouped[resource["category"]].append(resource)

    for category, label in RESOURCE_CATEGORY_LABELS.items():
        resources = grouped.get(category, [])
        if not resources:
            continue
        st.subheader(label)
        for resource in resources:
            with st.expander(resource["title"], expanded=False):
                st.caption(f"Audience: {resource['audience']}")
                for field_name in (
                    "template",
                    "example_output",
                    "glossary_entry",
                    "faq",
                    "internal_only_note",
                ):
                    value = resource.get(field_name)
                    if value:
                        st.markdown(value)


def render_home(data: dict, progress: dict[str, str]) -> None:
    st.title(data["title"])
    st.write(data["summary"])

    completed, total = completion_summary(data, progress)
    st.progress(completed / total if total else 0)
    st.caption(f"{completed} of {total} modules marked completed.")

    st.subheader("Recommended sequence")
    for nav_item in data["navigation"]:
        modules = modules_for_section(data, nav_item["id"])
        count = len(modules)
        st.markdown(f"- **{nav_item['title']}**: {nav_item['description']} ({count} module{'s' if count != 1 else ''})")

    st.subheader("Quick prompts to resume after class")
    st.code(
        "Inspect this repo and tell me the single best next step based on the self-paced guide.",
        language="text",
    )
    st.code(
        "Summarize what I last worked on in this repo and remind me how to validate the baseline before editing code.",
        language="text",
    )

    st.subheader("Starter briefs")
    for resource in resources_for_category(data, "starter_brief"):
        with st.expander(resource["title"]):
            st.markdown(resource["template"])


def main() -> None:
    data = load_guide_content()
    progress = load_progress()

    st.sidebar.title("Guide Navigation")
    completed, total = completion_summary(data, progress)
    st.sidebar.caption(f"Completed modules: {completed}/{total}")

    section_labels = {"home": "Home"}
    for nav_item in data["navigation"]:
        section_labels[nav_item["id"]] = nav_item["title"]
    section_labels["troubleshooting_resources"] = "Troubleshooting"

    selected_section = st.sidebar.radio(
        "Open section",
        options=list(section_labels.keys()),
        format_func=lambda section_id: section_labels[section_id],
    )

    st.sidebar.markdown("**Progress at a glance**")
    for module in data["modules"]:
        status = progress.get(module["id"], "Not started")
        st.sidebar.caption(f"{module['title']}: {status}")

    if selected_section == "home":
        render_home(data, progress)
        return

    if selected_section == "troubleshooting_resources":
        render_resources(data)
        return

    nav_item = next(item for item in data["navigation"] if item["id"] == selected_section)
    render_section(
        nav_item["title"],
        nav_item["description"],
        modules_for_section(data, selected_section),
        progress,
    )


if __name__ == "__main__":
    main()
