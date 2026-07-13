from pathlib import Path

def test_v425_docs():
    root = Path(__file__).resolve().parents[2]
    assert (root / "docs" / "v4_25" / "PLUGIN_POLICY_GATE.md").exists()
    assert (root / "docs" / "v4_25" / "EXECUTION_ISOLATION_CONTRACT.md").exists()
