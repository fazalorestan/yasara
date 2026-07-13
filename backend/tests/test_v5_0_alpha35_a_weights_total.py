from app.platform_core.portfolio_intelligence.allocation import PortfolioAllocationEngine

def test_v500_alpha35_a_weights_total(): assert PortfolioAllocationEngine().calculate_weights([{'symbol':'A','value':1}])['total_value']==1