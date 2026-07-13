from pathlib import Path

def test_v27_distribution_scripts_exist():
    root = Path(__file__).resolve().parents[1]
    assert (root / "scripts" / "apply_v2_7_distribution_router_patch.py").exists()
    assert (root / "scripts" / "build_v2_7_final_distribution.bat").exists()
    assert (root / "scripts" / "run_yasara_v2_7.bat").exists()
    assert (root / "scripts" / "create_v2_7_desktop_shortcut.bat").exists()
