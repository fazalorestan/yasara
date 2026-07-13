from app.platform_core.portfolio_intelligence.risk_score import PortfolioRiskScoreService

def test_v500_alpha35_b_risk_ready(): assert PortfolioRiskScoreService().score({}, {}, {})['ready'] is True