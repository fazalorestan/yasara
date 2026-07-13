from app.platform_core.portfolio_intelligence.analytics_service import PortfolioAnalyticsRiskService

def test_v500_alpha35_b_service_report():
 r=PortfolioAnalyticsRiskService().report(); assert r is not None
