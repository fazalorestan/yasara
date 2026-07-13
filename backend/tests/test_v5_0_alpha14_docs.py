from pathlib import Path
def test_v500_alpha14_docs():
    root = Path(__file__).resolve().parents[2]
    assert (root / "docs" / "v5_0_alpha_14" / "LICENSE_SUBSYSTEM_FINAL_READINESS.md").exists()
