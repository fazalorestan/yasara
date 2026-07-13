from pathlib import Path

def test_v448_docs():
    root = Path(__file__).resolve().parents[2]
    assert (root / "docs" / "v4_48" / "YASARA_INDICATOR_SETTINGS_PRESETS.md").exists()
