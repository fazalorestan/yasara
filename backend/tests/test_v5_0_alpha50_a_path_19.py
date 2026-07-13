from pathlib import Path

def test_path_19():
 root=Path(__file__).resolve().parents[2]; assert (root/'APPLY_V5_0_ALPHA_50_WINDOWS_REAL_EXE_PATCH.md').exists()
