from app.platform_core.portfolio_intelligence.analytics import PortfolioAnalyticsService

def test_v500_alpha35_b_summary_return(): assert PortfolioAnalyticsService().summary([100,110])['total_return_pct']==10