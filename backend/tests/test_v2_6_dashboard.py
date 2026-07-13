from app.v26_final_operational.service import FinalOperationalBridgeServiceV26

def test_v26_dashboard():
    d = FinalOperationalBridgeServiceV26().final_dashboard()
    assert d["ready"] is True
    assert d["quote"]["last"] > 0
    assert d["signal"]["confidence"] >= 0
    assert d["live_trading_enabled"] is False
