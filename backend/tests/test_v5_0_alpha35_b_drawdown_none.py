from app.platform_core.portfolio_intelligence.drawdown import PortfolioDrawdownAnalyzer

def test_v500_alpha35_b_drawdown_none(): assert PortfolioDrawdownAnalyzer().analyze([])['max_drawdown_pct']==0.0