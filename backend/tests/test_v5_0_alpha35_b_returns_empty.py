from app.platform_core.portfolio_intelligence.analytics import PortfolioAnalyticsService

def test_v500_alpha35_b_returns_empty(): assert PortfolioAnalyticsService().returns([1])['returns']==[]