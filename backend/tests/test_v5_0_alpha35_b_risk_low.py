from app.platform_core.portfolio_intelligence.risk_score import PortfolioRiskScoreService

def test_v500_alpha35_b_risk_low(): assert PortfolioRiskScoreService().score({'max_drawdown_pct':1},{'volatility':.01},{'concentration_ok':True})['risk_grade']=='low'