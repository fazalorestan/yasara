from pathlib import Path

def test_v500_alpha34_1_docs():
 root=Path(__file__).resolve().parents[2]; assert (root/'docs'/'v5_0_alpha_34_1'/'ROUTER_PROOF.md').exists()
