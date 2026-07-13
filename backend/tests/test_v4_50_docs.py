from pathlib import Path

def test_v450_docs():
    root = Path(__file__).resolve().parents[2]
    assert (root / "docs" / "v4_50" / "YASARA_INDICATOR_PLATFORM_HANDOFF.md").exists()
    assert (root / "docs" / "v4_50" / "INDICATOR_DEVELOPER_EXTENSION_GUIDE.md").exists()
