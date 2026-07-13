from app.v500_alpha35_portfolio_analytics_risk.service import PortfolioAnalyticsRiskFacadeV500Alpha35

def test_v500_alpha35_b_facade_returns():
 r=PortfolioAnalyticsRiskFacadeV500Alpha35().returns(); assert r is not None
