from pathlib import Path

def test_v438_docs():
    root = Path(__file__).resolve().parents[2]
    assert (root / "docs" / "v4_38" / "ENTERPRISE_CACHE.md").exists()
