from pathlib import Path

def test_v424_docs():
    root = Path(__file__).resolve().parents[2]
    assert (root / "docs" / "v4_24" / "PLUGIN_REGISTRY_SYNC.md").exists()
