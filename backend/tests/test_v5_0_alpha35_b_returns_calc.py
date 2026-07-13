from app.platform_core.portfolio_intelligence.analytics import PortfolioAnalyticsService

def test_v500_alpha35_b_returns_calc(): assert PortfolioAnalyticsService().returns([100,110])['returns'][0]==0.1