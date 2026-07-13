from pathlib import Path

def test_v500_alpha33_1_path_script():
 root=Path(__file__).resolve().parents[2]; assert (root/'backend/scripts/apply_v5_0_alpha_33_1_simple_patch_runner_fix.py').exists()
