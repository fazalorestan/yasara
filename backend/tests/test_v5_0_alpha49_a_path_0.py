from pathlib import Path

def test_path_0():
 root=Path(__file__).resolve().parents[2]; assert (root/'docs/v5_0_alpha_49/NATIVE_DESKTOP_APPLICATION_HOST_PACKAGE_A.md').exists()
