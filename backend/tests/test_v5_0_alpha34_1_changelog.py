from pathlib import Path

def test_v500_alpha34_1_changelog():
 root=Path(__file__).resolve().parents[2]; assert (root/'V5_0_ALPHA_34_1_ROUTER_PROOF_CHANGELOG.md').exists()
