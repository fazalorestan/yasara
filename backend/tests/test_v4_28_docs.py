from pathlib import Path

def test_v428_docs():
    root = Path(__file__).resolve().parents[2]
    assert (root / "docs" / "v4_28" / "PLUGIN_STATE_RUNTIME_SNAPSHOT.md").exists()
    assert (root / "docs" / "v4_28" / "STATE_PERSISTENCE_CONTRACT.md").exists()
