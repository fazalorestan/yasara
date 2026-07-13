from pathlib import Path

def test_v500_alpha41_b_path_script():
 root=Path(__file__).resolve().parents[2]; assert (root/'backend/scripts/apply_v5_0_alpha_41_strategy_scoring_patch.py').exists()
