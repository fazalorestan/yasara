from pathlib import Path

def test_v500_alpha5_docs():
    root = Path(__file__).resolve().parents[2]
    assert (root / "docs" / "v5_0_alpha_5" / "INDICATOR_PLATFORM_1000_TEST_RELEASE_GATE.md").exists()
