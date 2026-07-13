from app.platform_core.portfolio_intelligence.analytics_service import PortfolioAnalyticsRiskService

def test_v500_alpha35_b_service_volatility():
 r=PortfolioAnalyticsRiskService().volatility(); assert r is not None
