from app.platform_core.portfolio_intelligence.exposure import PortfolioExposureAnalyzer

def test_v500_alpha35_a_exposure_high(): assert PortfolioExposureAnalyzer().analyze([{'symbol':'A','value':90},{'symbol':'B','value':10}])['exposure_ok'] is False