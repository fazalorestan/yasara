from pathlib import Path

def test_v500_alpha7_docs():
    root = Path(__file__).resolve().parents[2]
    assert (root / "docs" / "v5_0_alpha_7" / "YASARA_RUNTIME_SIGNAL_LOGIC.md").exists()
