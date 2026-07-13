from pathlib import Path

def test_path_18():
 root=Path(__file__).resolve().parents[2]; assert (root/'backend/scripts/apply_v5_0_alpha_50_windows_real_exe_patch.py').exists()
