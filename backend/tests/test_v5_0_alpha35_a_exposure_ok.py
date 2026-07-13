from app.platform_core.portfolio_intelligence.exposure import PortfolioExposureAnalyzer

def test_v500_alpha35_a_exposure_ok(): assert PortfolioExposureAnalyzer().analyze([{'symbol':'A','value':50},{'symbol':'B','value':50}])['exposure_ok'] is True