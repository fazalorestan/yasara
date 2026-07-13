from app.platform_core.indicators.alerts.adapter import IndicatorSignalAlertAdapter

def test_v447_adapter():
    a = IndicatorSignalAlertAdapter().from_scanner_item({"symbol": "BTCUSDT", "direction": "LONG", "score": 88})
    assert a["indicator"] == "yasara"
    assert a["severity"] == "critical"
