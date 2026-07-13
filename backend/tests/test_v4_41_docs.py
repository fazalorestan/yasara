from pathlib import Path

def test_v441_docs():
    root = Path(__file__).resolve().parents[2]
    assert (root / "docs" / "v4_41" / "YASARA_INDICATOR_PLUGIN.md").exists()
