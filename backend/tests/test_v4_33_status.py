from app.platform_core.operations.status import OperationalStatusReporter

def test_v433_status():
    s = OperationalStatusReporter().report()
    assert s["ready"] is True
    assert s["no_new_trading_features"] is True
