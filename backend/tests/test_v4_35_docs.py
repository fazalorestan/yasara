from pathlib import Path

def test_v435_docs():
    root = Path(__file__).resolve().parents[2]
    assert (root / "docs" / "v4_35" / "ENTERPRISE_CONFIGURATION_CENTER.md").exists()
