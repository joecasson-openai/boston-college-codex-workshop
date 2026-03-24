"""
Central registry for workshop components.

This file is intentionally likely to become a merge-conflict hotspot because
every team will register new skills, plugins, or automations here.
"""

SKILL_CLASS_PATHS = [
    "campus_helper.skills.study_plan:StudyPlanSkill",
    "campus_helper.skills.study_spots:StudySpotsSkill",
    "campus_helper.skills.club_event_blurbs:ClubEventBlurbSkill",
    # TODO(workshop): add another skill path here during Challenge 1.
]

PLUGIN_CLASS_PATHS = [
    "campus_helper.plugins.campus_voice:CampusVoicePlugin",
    # TODO(workshop): add another plugin path here during Challenge 2.
]

SERVICE_CLASS_PATHS = [
    "campus_helper.services.study_spaces:StudySpacesService",
    "campus_helper.services.library_hours:LibraryHoursService",
    "campus_helper.services.dining:DiningService",
]

AUTOMATION_CLASS_PATHS = [
    "campus_helper.automations.morning_digest:MorningDigestAutomation",
    # TODO(workshop): add another automation path here during Challenge 4.
]
