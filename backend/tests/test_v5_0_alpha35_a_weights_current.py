from app.platform_core.portfolio_intelligence.allocation import PortfolioAllocationEngine

def test_v500_alpha35_a_weights_current(): assert PortfolioAllocationEngine().calculate_weights([{'symbol':'A','value':1}])['assets'][0]['current_weight']==1