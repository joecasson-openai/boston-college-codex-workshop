from pathlib import Path
import sys

REPO_ROOT = Path(__file__).resolve().parents[1]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from campus_helper.guide import load_guide_content, render_guide_markdown


OUTPUT_PATH = REPO_ROOT / "exports" / "student_self_paced_guide.md"


def main() -> None:
    data = load_guide_content()
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(render_guide_markdown(data))
    print(f"Wrote {OUTPUT_PATH.relative_to(REPO_ROOT)}")


if __name__ == "__main__":
    main()
