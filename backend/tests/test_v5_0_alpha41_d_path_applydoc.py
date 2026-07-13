from pathlib import Path

def test_v500_alpha41_d_path_applydoc():
 root=Path(__file__).resolve().parents[2]; assert (root/'APPLY_V5_0_ALPHA_41_STRATEGY_SIMULATION_PATCH.md').exists()
