from pathlib import Path

def test_v500_alpha38_b_path_changelog():
 root=Path(__file__).resolve().parents[2]; assert (root/'V5_0_ALPHA_38_EXCHANGE_MARKET_DATA_CHANGELOG.md').exists()
