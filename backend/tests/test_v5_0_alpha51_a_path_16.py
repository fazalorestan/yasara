from pathlib import Path

def test_path_16():
 root=Path(__file__).resolve().parents[2]; assert (root/'V5_0_ALPHA_51_EXE_SMOKE_BUILD_CHANGELOG.md').exists()
