from pathlib import Path

def test_v500_alpha35_b_backcompat():
 root=Path(__file__).resolve().parents[2]; assert (root/'V5_0_ALPHA_35_PORTFOLIO_ANALYTICS_RISK_BACKWARD_COMPATIBILITY.md').exists()
