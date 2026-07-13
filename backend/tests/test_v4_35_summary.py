from app.v435_configuration_center.models import ConfigurationCenterSummaryV435

def test_v435_summary():
    s = ConfigurationCenterSummaryV435()
    assert s.ready is True
    assert s.no_new_trading_features is True
    assert s.live_execution_enabled is False
