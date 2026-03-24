import tempfile
import unittest
from pathlib import Path

from campus_helper.guide import (
    GUIDE_CONTENT_PATH,
    load_guide_content,
    load_progress,
    render_guide_markdown,
    save_progress,
)


class GuideTests(unittest.TestCase):
    def test_guide_content_loads_and_has_required_sections(self):
        guide = load_guide_content()

        self.assertTrue(GUIDE_CONTENT_PATH.exists())
        self.assertEqual(guide["navigation"][0]["title"], "Start Here")
        self.assertGreaterEqual(len(guide["modules"]), 10)

    def test_render_markdown_contains_expected_headings(self):
        guide = load_guide_content()
        rendered = render_guide_markdown(guide)

        self.assertIn("# Campus Helper Student Self-Paced Codex Guide", rendered)
        self.assertIn("## Module 1: Start Here and Re-Enter the Workshop", rendered)
        self.assertIn("## Resources", rendered)

    def test_progress_round_trip(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            progress_path = Path(temp_dir) / "progress.json"
            save_progress({"module-1-start-here": "Completed"}, path=progress_path)
            loaded = load_progress(path=progress_path)

        self.assertEqual(loaded["module-1-start-here"], "Completed")


if __name__ == "__main__":
    unittest.main()
