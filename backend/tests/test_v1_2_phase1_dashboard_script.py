from pathlib import Path

def test_dashboard_patch_scripts_exist():
    root = Path(__file__).resolve().parents[1]
    assert (root / "scripts" / "apply_v1_2_phase1_dashboard_shell_patch.py").exists()
    assert (root / "scripts" / "update_windows_launcher_for_dashboard.bat").exists()
