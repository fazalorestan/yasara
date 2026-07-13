from pathlib import Path

def test_v439_docs():
    root = Path(__file__).resolve().parents[2]
    assert (root / "docs" / "v4_39" / "ENTERPRISE_STORAGE.md").exists()
