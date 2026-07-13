from app.platform_core.portfolio_intelligence.action_plan import PortfolioActionPlanService

def test_v500_alpha35_c_action_plan_actions(): assert isinstance(PortfolioActionPlanService().plan()['rebalance_actions'], list)
