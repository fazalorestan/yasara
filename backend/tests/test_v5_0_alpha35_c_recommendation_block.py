from app.platform_core.portfolio_intelligence.decision_support import PortfolioDecisionSupportService

def test_v500_alpha35_c_recommendation_block(): assert PortfolioDecisionSupportService().recommendation()['execution_allowed'] is False