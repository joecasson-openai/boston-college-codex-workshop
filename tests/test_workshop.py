import unittest

from campus_helper.runtime import load_workshop


class WorkshopTests(unittest.TestCase):
    def test_workshop_loads_core_components(self):
        workshop = load_workshop()

        self.assertIn("study_plan", workshop.skills)
        self.assertIn("study_spots", workshop.skills)
        self.assertIn("campus_voice", workshop.plugins)
        self.assertIn("morning_digest", workshop.automations)
        self.assertIn("study_spaces", workshop.services)

    def test_study_plan_skill_returns_expected_sections(self):
        workshop = load_workshop()
        output = workshop.skills["study_plan"].run(
            {
                "student_name": "Alex",
                "courses": "Biology, Calculus",
                "goal": "Prepare for Thursday's quiz.",
                "available_hours": 6,
                "constraints": "Lab report due Friday.",
            },
            workshop.services,
        )

        self.assertIn("Study Plan for Alex", output)
        self.assertIn("Recommended blocks", output)

    def test_morning_digest_automation_runs(self):
        workshop = load_workshop()
        output = workshop.automations["morning_digest"].run(
            {
                "student_name": "Alex",
                "day": "Tuesday",
                "dining_hall": "Hillside Cafe",
            },
            workshop.services,
        )

        self.assertIn("Morning Digest for Alex", output)
        self.assertIn("Hillside Cafe", output)


if __name__ == "__main__":
    unittest.main()
