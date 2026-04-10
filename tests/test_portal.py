import unittest

from bc_portal import create_app


class PortalTests(unittest.TestCase):
    def setUp(self):
        self.app = create_app().test_client()

    def test_dashboard_renders_service_cards(self):
        response = self.app.get("/")

        self.assertEqual(response.status_code, 200)
        body = response.data.decode()
        self.assertIn("Academic Advising", body)
        self.assertIn("Campus Life", body)
        self.assertIn("Study Spaces", body)

    def test_academic_advising_service_generates_plan(self):
        response = self.app.post(
            "/services/academic-advising",
            data={
                "student_name": "Maya Johnson",
                "priority": "Prepare for midterms",
                "weekly_hours": "10",
                "include_career_note": "on",
            },
        )

        self.assertEqual(response.status_code, 200)
        body = response.data.decode()
        self.assertIn("Academic Advising.", body)
        self.assertIn("Maya Johnson&#39;s advising plan", body)
        self.assertIn("Weekly study hours", body)

    def test_campus_life_service_generates_announcement(self):
        response = self.app.post(
            "/services/campus-life",
            data={
                "club_name": "BC Coding Club",
                "event_name": "Builder Night",
                "audience": "first-year students",
                "tone": "Warm and welcoming",
            },
        )

        self.assertEqual(response.status_code, 200)
        body = response.data.decode()
        self.assertIn("Builder Night announcement draft", body)
        self.assertIn("BC Coding Club", body)

    def test_study_spaces_service_returns_recommendations(self):
        response = self.app.post(
            "/services/study-spaces",
            data={
                "study_style": "Quiet focus",
                "day": "Tuesday",
                "needs_outlets": "on",
            },
        )

        self.assertEqual(response.status_code, 200)
        body = response.data.decode()
        self.assertIn("Top recommendation", body)
        self.assertIn("Nearby dining", body)

    def test_unknown_service_returns_404(self):
        response = self.app.get("/services/not-a-service")

        self.assertEqual(response.status_code, 404)


if __name__ == "__main__":
    unittest.main()
