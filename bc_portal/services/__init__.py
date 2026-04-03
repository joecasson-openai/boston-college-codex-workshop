from bc_portal.services import academic_advising, campus_life, study_spaces


SERVICE_MODULES = {
    academic_advising.SERVICE_CARD["slug"]: academic_advising,
    campus_life.SERVICE_CARD["slug"]: campus_life,
    study_spaces.SERVICE_CARD["slug"]: study_spaces,
}


def get_service_module(slug: str):
    return SERVICE_MODULES.get(slug)


def get_dashboard_cards() -> list[dict]:
    return [service.SERVICE_CARD for service in SERVICE_MODULES.values()]
