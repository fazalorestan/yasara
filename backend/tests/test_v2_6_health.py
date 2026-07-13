from app.v26_final_operational.service import FinalOperationalBridgeServiceV26

def test_v26_health():
    h = FinalOperationalBridgeServiceV26().health()
    assert h["ready"] is True
    assert h["operational_progress_percent"] == 100
    assert h["live_trading_enabled"] is False
