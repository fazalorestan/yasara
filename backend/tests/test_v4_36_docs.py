from pathlib import Path

def test_v436_docs():
    root = Path(__file__).resolve().parents[2]
    assert (root / "docs" / "v4_36" / "ENTERPRISE_SCHEDULER.md").exists()
