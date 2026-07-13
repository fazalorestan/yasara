from pathlib import Path

def test_v500_alpha35_b_script():
 root=Path(__file__).resolve().parents[2]; assert (root/'backend'/'scripts'/'apply_v5_0_alpha_35_portfolio_analytics_risk_patch.py').exists()
