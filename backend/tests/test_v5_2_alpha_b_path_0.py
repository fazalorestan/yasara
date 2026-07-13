from pathlib import Path

def test_path_0():
 root=Path(__file__).resolve().parents[2]; assert (root/'docs/v5_2_alpha/FIRST_REAL_WINDOWS_EXE_BUILD_PACKAGE_B.md').exists()
