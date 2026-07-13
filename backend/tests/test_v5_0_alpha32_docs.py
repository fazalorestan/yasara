from pathlib import Path

def test_v500_alpha32_docs():
 root=Path(__file__).resolve().parents[2]; assert (root/'docs'/'v5_0_alpha_32'/'STRATEGY_OPTIMIZER_PRO.md').exists()
