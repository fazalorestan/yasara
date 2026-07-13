from app.platform_core.portfolio_intelligence.optimizer_link import PortfolioOptimizerLinkService

def test_v500_alpha35_c_opt_block(): assert PortfolioOptimizerLinkService().allocation_bias()['execution_allowed'] is False