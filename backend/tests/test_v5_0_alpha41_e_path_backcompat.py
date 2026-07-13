from pathlib import Path

def test_v500_alpha41_e_path_backcompat():
 root=Path(__file__).resolve().parents[2]; assert (root/'V5_0_ALPHA_41_STRATEGY_ENTERPRISE_BACKWARD_COMPATIBILITY.md').exists()
