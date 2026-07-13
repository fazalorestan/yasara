from pathlib import Path

def test_path_16():
 root=Path(__file__).resolve().parents[2]; assert (root/'backend/scripts/apply_v5_0_alpha_49_native_desktop_patch.py').exists()
