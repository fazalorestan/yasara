from pathlib import Path

def test_path_0():
 root=Path(__file__).resolve().parents[2]; assert (root/'docs/v5_0_alpha_49/FIRST_INTERNAL_WINDOWS_PORTABLE_BUILD_PACKAGE_D.md').exists()
