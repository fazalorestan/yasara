from app.platform_core.portfolio_intelligence.exposure import PortfolioExposureAnalyzer

def test_v500_alpha35_a_exposure_empty(): assert PortfolioExposureAnalyzer().analyze([])['top_symbol'] is None