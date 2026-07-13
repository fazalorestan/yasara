from app.platform_core.portfolio_intelligence.optimizer_link import PortfolioOptimizerLinkService

def test_v500_alpha35_c_opt_best(): assert PortfolioOptimizerLinkService().optimizer_best()['ready'] is True