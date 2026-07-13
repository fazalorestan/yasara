from pathlib import Path

def test_v446_docs():
    root = Path(__file__).resolve().parents[2]
    assert (root / "docs" / "v4_46" / "YASARA_INDICATOR_SCANNER_WATCHLIST.md").exists()
