from pathlib import Path

def test_v429_docs():
    root = Path(__file__).resolve().parents[2]
    assert (root / "docs" / "v4_29" / "TIMEZONE_SAFE_RUNTIME.md").exists()
