from pathlib import Path

def test_path_0():
 root=Path(__file__).resolve().parents[2]; assert (root/'docs/v5_2_alpha/NATIVE_WINDOWS_LAUNCHER_DASHBOARD_BOOTSTRAP_PACKAGE_D.md').exists()
