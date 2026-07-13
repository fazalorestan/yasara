from pathlib import Path

def test_v423_documentation():
    pass

    root = Path(__file__).resolve().parents[2]
    docs = root / "docs" / "v4_23"
    assert (docs / "PLUGIN_MANIFEST_CATALOG.md").exists()
    assert (docs / "GOVERNANCE_BRIDGE.md").exists()
