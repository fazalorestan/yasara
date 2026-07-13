from app.platform_core.portfolio_intelligence.analytics_service import PortfolioAnalyticsRiskService

def test_v500_alpha35_b_report_block(): assert PortfolioAnalyticsRiskService().report()['execution_allowed'] is False
