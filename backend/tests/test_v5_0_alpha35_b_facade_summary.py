from app.v500_alpha35_portfolio_analytics_risk.service import PortfolioAnalyticsRiskFacadeV500Alpha35

def test_v500_alpha35_b_facade_summary():
 r=PortfolioAnalyticsRiskFacadeV500Alpha35().summary(); assert r is not None
