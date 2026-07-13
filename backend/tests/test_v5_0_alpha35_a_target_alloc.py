from app.platform_core.portfolio_intelligence.allocation import PortfolioAllocationEngine

def test_v500_alpha35_a_target_alloc(): assert PortfolioAllocationEngine().target_allocation([{'symbol':'A','target_weight':.5}],100)['items'][0]['target_value']==50