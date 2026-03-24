from dataclasses import dataclass
from importlib import import_module
from typing import Any

from campus_helper.workshop_registry import (
    AUTOMATION_CLASS_PATHS,
    PLUGIN_CLASS_PATHS,
    SERVICE_CLASS_PATHS,
    SKILL_CLASS_PATHS,
)


@dataclass
class WorkshopBundle:
    skills: dict[str, Any]
    plugins: dict[str, Any]
    automations: dict[str, Any]
    services: dict[str, Any]
    warnings: list[str]


def import_from_path(path: str) -> Any:
    module_name, class_name = path.split(":")
    module = import_module(module_name)
    return getattr(module, class_name)


def build_catalog(paths: list[str], id_attr: str, label: str):
    loaded = {}
    warnings = []

    for path in paths:
        try:
            klass = import_from_path(path)
            instance = klass()
            loaded[getattr(instance, id_attr)] = instance
        except Exception as exc:  # pragma: no cover - warning path used in workshop UI
            warnings.append(f"{label}: failed to load {path} ({exc})")

    return loaded, warnings


def load_workshop() -> WorkshopBundle:
    services, service_warnings = build_catalog(SERVICE_CLASS_PATHS, "service_name", "service")
    skills, skill_warnings = build_catalog(SKILL_CLASS_PATHS, "skill_id", "skill")
    plugins, plugin_warnings = build_catalog(PLUGIN_CLASS_PATHS, "plugin_id", "plugin")
    automations, automation_warnings = build_catalog(
        AUTOMATION_CLASS_PATHS,
        "automation_id",
        "automation",
    )

    return WorkshopBundle(
        skills=skills,
        plugins=plugins,
        automations=automations,
        services=services,
        warnings=service_warnings + skill_warnings + plugin_warnings + automation_warnings,
    )
