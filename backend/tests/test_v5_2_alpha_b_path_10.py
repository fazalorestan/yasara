from pathlib import Path

def test_path_10():
 root=Path(__file__).resolve().parents[2]; assert (root/'V5_2_ALPHA_FIRST_REAL_EXE_BUILD_CHANGELOG.md').exists()
