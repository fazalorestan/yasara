from pathlib import Path
def test_v500_alpha14_router():
    root = Path(__file__).resolve().parents[2]
    assert (root / "backend" / "scripts" / "apply_v5_0_alpha_14_license_readiness_router_patch.py").exists()
