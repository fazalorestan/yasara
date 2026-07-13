from app.platform_core.portfolio_intelligence.optimizer_link import PortfolioOptimizerLinkService

def test_v500_alpha35_c_opt_bias(): assert PortfolioOptimizerLinkService().allocation_bias()['bias'] in ['increase','hold']