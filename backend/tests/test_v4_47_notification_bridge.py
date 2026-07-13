from app.platform_core.indicators.alerts.notification_bridge import IndicatorNotificationBridge

def test_v447_notification_bridge():
    r = IndicatorNotificationBridge().publish({"symbol": "BTCUSDT"})
    assert r["ready"] is True
    assert r["event"]["name"] == "IndicatorNotificationRequested"
