from pathlib import Path

def test_path_18():
 root=Path(__file__).resolve().parents[2]; assert (root/'backend/scripts/apply_v5_0_alpha_48_windows_builder_patch.py').exists()
