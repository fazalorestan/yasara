from app.v447_indicator_alert_notification.service import IndicatorAlertNotificationFacadeV447

def test_v447_facade():
    f = IndicatorAlertNotificationFacadeV447()
    assert f.summary().ready is True
    assert f.contract()["execution_allowed"] is False
    assert f.sample_alert()["ready"] is True
