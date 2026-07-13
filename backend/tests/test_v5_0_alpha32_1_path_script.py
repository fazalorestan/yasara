from pathlib import Path

def test_v500_alpha32_1_path_script():
 root=Path(__file__).resolve().parents[2]; assert (root/'backend/scripts/apply_v5_0_alpha_32_1_definitive_patch_runner_hotfix.py').exists()
