from pathlib import Path

def test_v500_alpha35_b_route():
 root=Path(__file__).resolve().parents[2]; assert (root/'backend'/'app'/'api'/'v1'/'routes'/'v500_alpha35_portfolio_analytics_risk_v1.py').exists()
