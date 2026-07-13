from pathlib import Path

def test_v26_scripts():
    root = Path(__file__).resolve().parents[1]
    assert (root / "scripts" / "apply_v2_6_final_operational_router_patch.py").exists()
    assert (root / "scripts" / "build_v2_6_operational_release.bat").exists()
