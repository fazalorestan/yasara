from app.platform_core.portfolio_intelligence.concentration import PortfolioConcentrationRiskService

def test_v500_alpha35_b_concentration_bad(): assert PortfolioConcentrationRiskService().analyze([{'symbol':'A','value':90},{'symbol':'B','value':10}])['concentration_ok'] is False