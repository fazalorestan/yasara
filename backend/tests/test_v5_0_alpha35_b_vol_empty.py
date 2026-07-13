from app.platform_core.portfolio_intelligence.volatility import PortfolioVolatilityAnalyzer

def test_v500_alpha35_b_vol_empty(): assert PortfolioVolatilityAnalyzer().calculate([])['volatility']==0.0