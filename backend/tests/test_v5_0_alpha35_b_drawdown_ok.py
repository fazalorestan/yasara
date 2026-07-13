from app.platform_core.portfolio_intelligence.drawdown import PortfolioDrawdownAnalyzer

def test_v500_alpha35_b_drawdown_ok(): assert PortfolioDrawdownAnalyzer().analyze([100,90])['drawdown_ok'] is True