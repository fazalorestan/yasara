from pathlib import Path

def test_v500_alpha37_b_path_changelog():
 root=Path(__file__).resolve().parents[2]; assert (root/'V5_0_ALPHA_37_BROKER_ORDERS_ACCOUNT_CHANGELOG.md').exists()
