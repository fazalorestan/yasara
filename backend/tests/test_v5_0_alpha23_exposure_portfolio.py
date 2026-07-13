from app.platform_core.risk_engine.exposure import ExposureGuard

def test_v500_alpha23_exposure_portfolio(): assert ExposureGuard().check_portfolio_exposure(50,60)['allowed'] is True
