from app.v11_alerts.service import AlertsNotificationServiceV11

def test_alerts_service_demo():
    snapshot = AlertsNotificationServiceV11().demo()
    assert snapshot.ready is True
    assert len(snapshot.rules) >= 1
    assert len(snapshot.events) >= 2
