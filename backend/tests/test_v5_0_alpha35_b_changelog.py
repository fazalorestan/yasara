from pathlib import Path

def test_v500_alpha35_b_changelog():
 root=Path(__file__).resolve().parents[2]; assert (root/'V5_0_ALPHA_35_PORTFOLIO_ANALYTICS_RISK_CHANGELOG.md').exists()
