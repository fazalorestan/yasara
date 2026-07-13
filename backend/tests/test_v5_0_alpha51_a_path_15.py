from pathlib import Path

def test_path_15():
 root=Path(__file__).resolve().parents[2]; assert (root/'APPLY_V5_0_ALPHA_51_EXE_SMOKE_BUILD_PATCH.md').exists()
