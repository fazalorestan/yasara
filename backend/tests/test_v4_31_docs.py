from pathlib import Path

def test_v431_docs():
    root = Path(__file__).resolve().parents[2]
    assert (root / "docs" / "v4_31" / "RELEASE_READINESS_GATE.md").exists()
