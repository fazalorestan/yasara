from app.platform_core.portfolio_intelligence.concentration import PortfolioConcentrationRiskService

def test_v500_alpha35_b_concentration_ok(): assert PortfolioConcentrationRiskService().analyze([{'symbol':'A','value':50},{'symbol':'B','value':50}])['concentration_ok'] is True