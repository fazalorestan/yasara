from pathlib import Path

def test_v442_docs():
    root = Path(__file__).resolve().parents[2]
    assert (root / "docs" / "v4_42" / "YASARA_INDICATOR_CHART_INTEGRATION.md").exists()
