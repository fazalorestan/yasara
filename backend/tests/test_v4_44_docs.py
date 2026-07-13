from pathlib import Path

def test_v444_docs():
    root = Path(__file__).resolve().parents[2]
    assert (root / "docs" / "v4_44" / "YASARA_INDICATOR_PINE_SOURCE_ARCHIVE.md").exists()
