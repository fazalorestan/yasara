from pathlib import Path

def test_path_16():
 root=Path(__file__).resolve().parents[2]; assert (root/'APPLY_V5_0_ALPHA_50_WINDOWS_EXE_BUILD_PATCH.md').exists()
