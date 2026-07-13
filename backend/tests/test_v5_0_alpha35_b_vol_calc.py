from app.platform_core.portfolio_intelligence.volatility import PortfolioVolatilityAnalyzer

def test_v500_alpha35_b_vol_calc(): assert PortfolioVolatilityAnalyzer().calculate([0.1,-0.1])['ready'] is True