from pathlib import Path

def test_path_9():
 root=Path(__file__).resolve().parents[2]; assert (root/'APPLY_V5_2_ALPHA_FIRST_REAL_EXE_BUILD_PATCH.md').exists()
