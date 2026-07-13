from pathlib import Path

def test_path_0():
 root=Path(__file__).resolve().parents[2]; assert (root/'docs/v5_0_alpha_49/DESKTOP_DASHBOARD_GUI_SHELL_PACKAGE_B.md').exists()
