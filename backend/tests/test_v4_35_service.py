from app.v435_configuration_center.service import ConfigurationCenterServiceV435

def test_v435_service():
    s = ConfigurationCenterServiceV435()
    assert s.summary().ready is True
    assert s.profiles()["ready"] is True
    assert s.snapshot()["no_new_trading_features"] is True
