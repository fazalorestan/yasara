from app.platform_core.portfolio_intelligence.decision_support import PortfolioDecisionSupportService

def test_v500_alpha35_c_recommendation(): assert PortfolioDecisionSupportService().recommendation()['action'] in ['reduce_risk','increase_allocation','hold','rebalance_only']