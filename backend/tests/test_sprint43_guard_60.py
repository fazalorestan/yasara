from app.v52_enterprise_trading_os.service import EnterpriseTradingOSService

def test_guard():
    s = EnterpriseTradingOSService().snapshot()
    assert s.signal_only_default is True
    assert s.auto_trading_enabled is False
