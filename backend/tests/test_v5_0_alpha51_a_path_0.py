from pathlib import Path

def test_path_0():
 root=Path(__file__).resolve().parents[2]; assert (root/'docs/v5_0_alpha_51/FIRST_INTERNAL_WINDOWS_EXE_SMOKE_BUILD_PACKAGE_A.md').exists()
