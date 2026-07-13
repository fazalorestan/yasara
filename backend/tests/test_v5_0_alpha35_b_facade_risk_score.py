from app.v500_alpha35_portfolio_analytics_risk.service import PortfolioAnalyticsRiskFacadeV500Alpha35

def test_v500_alpha35_b_facade_risk_score():
 r=PortfolioAnalyticsRiskFacadeV500Alpha35().risk_score(); assert r is not None
