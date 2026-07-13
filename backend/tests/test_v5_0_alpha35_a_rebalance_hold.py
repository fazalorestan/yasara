from app.platform_core.portfolio_intelligence.rebalance import PortfolioRebalancePlanner

def test_v500_alpha35_a_rebalance_hold(): assert PortfolioRebalancePlanner().plan({'total_value':100,'assets':[{'symbol':'A','value':50,'target_weight':.5,'current_weight':.5}]})['actions'][0]['action']=='hold'