from app.platform_core.portfolio_intelligence.rebalance import PortfolioRebalancePlanner

def test_v500_alpha35_a_rebalance_block(): assert PortfolioRebalancePlanner().plan({'total_value':0,'assets':[]})['execution_allowed'] is False