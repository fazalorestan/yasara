from pathlib import Path

def test_v2_0_final_release_scripts_exist():
    root = Path(__file__).resolve().parents[1]
    assert (root / "scripts" / "apply_v2_0_final_release_router_patch.py").exists()
    assert (root / "scripts" / "build_v2_0_final_release.bat").exists()
    assert (root / "scripts" / "run_v2_0_final.bat").exists()
