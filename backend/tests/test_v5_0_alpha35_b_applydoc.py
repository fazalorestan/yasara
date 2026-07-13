from pathlib import Path

def test_v500_alpha35_b_applydoc():
 root=Path(__file__).resolve().parents[2]; assert (root/'APPLY_V5_0_ALPHA_35_PORTFOLIO_ANALYTICS_RISK_PATCH.md').exists()
