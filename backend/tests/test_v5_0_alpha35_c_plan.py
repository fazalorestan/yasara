from app.platform_core.portfolio_intelligence.action_plan import PortfolioActionPlanService

def test_v500_alpha35_c_plan(): assert PortfolioActionPlanService().plan()['ready'] is True