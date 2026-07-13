from app.platform_core.indicators.alerts.service import IndicatorAlertNotificationService

def test_v447_service():
    s = IndicatorAlertNotificationService()
    r = s.build_alert({"symbol": "BTCUSDT", "direction": "LONG", "score": 88})
    assert r["ready"] is True
    assert r["execution_allowed"] is False
