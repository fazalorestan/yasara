from pathlib import Path

def test_v500_alpha41_d_path_script():
 root=Path(__file__).resolve().parents[2]; assert (root/'backend/scripts/apply_v5_0_alpha_41_strategy_simulation_patch.py').exists()
