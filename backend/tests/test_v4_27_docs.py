from pathlib import Path

def test_v427_docs():
    root = Path(__file__).resolve().parents[2]
    assert (root / "docs" / "v4_27" / "EXTENSION_HOST_SANDBOX.md").exists()
    assert (root / "docs" / "v4_27" / "PLUGIN_SANDBOX_RULES.md").exists()
