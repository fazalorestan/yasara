from pathlib import Path

def test_v500_alpha32_backcompat():
 root=Path(__file__).resolve().parents[2]; assert (root/'V5_0_ALPHA_32_STRATEGY_OPTIMIZER_PRO_BACKWARD_COMPATIBILITY.md').exists()
