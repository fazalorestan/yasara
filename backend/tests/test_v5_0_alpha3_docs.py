from pathlib import Path

def test_v500_alpha3_docs():
    root = Path(__file__).resolve().parents[2]
    assert (root / "docs" / "v5_0_alpha_3" / "INDICATOR_SANDBOX_VALIDATION.md").exists()
