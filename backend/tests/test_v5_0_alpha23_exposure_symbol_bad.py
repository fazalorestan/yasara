from app.platform_core.risk_engine.exposure import ExposureGuard

def test_v500_alpha23_exposure_symbol_bad(): assert ExposureGuard().check_symbol_exposure(30,20)['allowed'] is False
