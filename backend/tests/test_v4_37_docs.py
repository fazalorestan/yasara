from pathlib import Path

def test_v437_docs():
    root = Path(__file__).resolve().parents[2]
    assert (root / "docs" / "v4_37" / "ENTERPRISE_QUEUE.md").exists()
