from pathlib import Path

def test_path_10():
 root=Path(__file__).resolve().parents[2]; assert (root/'APPLY_V5_2_ALPHA_NATIVE_LAUNCHER_PATCH.md').exists()
