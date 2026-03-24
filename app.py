import json
from typing import Any

import streamlit as st

from campus_helper.runtime import load_workshop


st.set_page_config(
    page_title="Campus Helper Agent Workshop",
    page_icon="🧭",
    layout="wide",
)


def render_field(field: dict[str, Any], prefix: str = "") -> Any:
    key = f"{prefix}{field['key']}"
    field_type = field.get("type", "text")
    label = field["label"]
    help_text = field.get("help")
    default = field.get("default")

    if field_type == "textarea":
        return st.text_area(label, value=default or "", help=help_text, key=key)
    if field_type == "select":
        options = field.get("options", [])
        if default in options:
            index = options.index(default)
        else:
            index = 0
        return st.selectbox(label, options=options, index=index, help=help_text, key=key)
    if field_type == "number":
        return st.number_input(
            label,
            min_value=field.get("min_value", 0),
            max_value=field.get("max_value", 20),
            value=default if default is not None else field.get("min_value", 0),
            step=field.get("step", 1),
            help=help_text,
            key=key,
        )
    if field_type == "checkbox":
        return st.checkbox(label, value=bool(default), help=help_text, key=key)
    return st.text_input(label, value=default or "", help=help_text, key=key)


def apply_plugins(workshop, selected_plugin_ids, output, skill, inputs):
    for plugin_id in selected_plugin_ids:
        plugin = workshop.plugins[plugin_id]
        output = plugin.apply(
            content=output,
            skill=skill,
            inputs=inputs,
            services=workshop.services,
        )
    return output


def show_sidebar(workshop):
    st.sidebar.title("Workshop Map")
    st.sidebar.markdown(
        """
        This starter app is intentionally modular.

        - `skills/` generate useful behavior
        - `plugins/` visibly change output
        - `services/` act like local tool-backed data sources
        - `automations/` simulate scheduled or triggered actions
        """
    )

    st.sidebar.caption("Loaded components")
    st.sidebar.write(f"Skills: {len(workshop.skills)}")
    st.sidebar.write(f"Plugins: {len(workshop.plugins)}")
    st.sidebar.write(f"Automations: {len(workshop.automations)}")
    st.sidebar.write(f"Services: {len(workshop.services)}")

    if workshop.warnings:
        st.sidebar.warning("Some optional components did not load. That is intentional for the workshop.")
        for warning in workshop.warnings:
            st.sidebar.code(warning)


def playground_tab(workshop):
    st.subheader("Agent Playground")
    st.write("Pick a skill, fill in the form, and optionally layer a plugin on top of the result.")

    skill = st.selectbox(
        "Choose a skill",
        options=list(workshop.skills.values()),
        format_func=lambda item: item.name,
    )

    with st.form("skill-form", clear_on_submit=False):
        rendered_inputs = {
            field["key"]: render_field(field, prefix=f"{skill.skill_id}-")
            for field in skill.input_fields
        }
        selected_plugins = st.multiselect(
            "Optional plugins",
            options=list(workshop.plugins.keys()),
            format_func=lambda plugin_id: workshop.plugins[plugin_id].name,
            help="Plugins do not change the core skill logic. They only transform or decorate the final output.",
        )
        submitted = st.form_submit_button("Run selected skill")

    if submitted:
        output = skill.run(rendered_inputs, workshop.services)
        output = apply_plugins(workshop, selected_plugins, output, skill, rendered_inputs)

        left, right = st.columns([3, 2])
        with left:
            st.markdown(output)
        with right:
            st.markdown("#### Input Payload")
            st.code(json.dumps(rendered_inputs, indent=2), language="json")
            st.markdown("#### Ask Codex Next")
            st.info(skill.next_prompt_hint)


def automations_tab(workshop):
    st.subheader("Automation Simulator")
    st.write("These automations are local and button-triggered so students can reason about behavior without a real scheduler.")

    automation = st.selectbox(
        "Choose an automation",
        options=list(workshop.automations.values()),
        format_func=lambda item: item.name,
    )

    with st.form("automation-form", clear_on_submit=False):
        rendered_inputs = {
            field["key"]: render_field(field, prefix=f"{automation.automation_id}-")
            for field in automation.input_fields
        }
        submitted = st.form_submit_button("Simulate automation run")

    if submitted:
        st.markdown(automation.run(rendered_inputs, workshop.services))


def services_tab(workshop):
    st.subheader("Local Tool Services")
    st.write("These services are lightweight stand-ins for MCP-style tools. They read local JSON, normalize data, and hand it to skills or automations.")

    study_spaces = workshop.services["study_spaces"].list_spots()
    dining_preview = workshop.services["dining"].list_halls()

    left, right = st.columns(2)
    with left:
        st.markdown("#### Study Spaces")
        st.json(study_spaces[:2])
    with right:
        st.markdown("#### Dining Halls")
        st.json(dining_preview[:2])

    with st.expander("Open service contract notes"):
        st.markdown(
            """
            - Study spots use `study_spaces.json`
            - Library hours use `library_hours.json`
            - Dining uses `dining_halls.json`

            Students will need to inspect both service code and the consuming skill code during the workshop.
            """
        )


def main():
    st.title("Campus Helper Agent")
    st.caption("A starter repository for AI-assisted coding workflows with Codex.")

    workshop = load_workshop()
    show_sidebar(workshop)

    overview, playground, automations, services = st.tabs(
        ["Overview", "Playground", "Automations", "Services"]
    )

    with overview:
        st.markdown(
            """
            ### What this app does

            The Campus Helper Agent helps with:

            - study planning
            - study spot recommendations
            - club event blurb drafting
            - daily reminder or digest-style outputs

            ### What students practice

            - inspecting a multi-file codebase
            - fixing a small but realistic bug
            - adding a new skill
            - adding a plugin without rewriting the app
            - wiring a local tool-backed service
            - extending an automation pattern
            """
        )
        st.markdown("Open `WORKSHOP_CHALLENGES.md` for the guided sequence.")

    with playground:
        playground_tab(workshop)

    with automations:
        automations_tab(workshop)

    with services:
        services_tab(workshop)


if __name__ == "__main__":
    main()
