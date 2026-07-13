from pathlib import Path

def test_path_18():
 root=Path(__file__).resolve().parents[2]; assert (root/'APPLY_V5_0_ALPHA_46_DESKTOP_HOST_PATCH.md').exists()
