from pathlib import Path

def test_path_0():
 root=Path(__file__).resolve().parents[2]; assert (root/'docs/v5_0_alpha_50/FIRST_REAL_WINDOWS_EXE_BUILD_PIPELINE_PACKAGE_A.md').exists()
