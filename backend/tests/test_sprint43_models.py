from app.v52_enterprise_trading_os.models import TradingOSSnapshot

def test_snapshot_defaults():
    s = TradingOSSnapshot()
    assert s.real_data_only is True
    assert s.mock_data is False
    assert s.auto_trading_enabled is False
