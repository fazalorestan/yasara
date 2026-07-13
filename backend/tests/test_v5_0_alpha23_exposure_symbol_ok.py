from app.platform_core.risk_engine.exposure import ExposureGuard

def test_v500_alpha23_exposure_symbol_ok(): assert ExposureGuard().check_symbol_exposure(10,20)['allowed'] is True
