from app.v447_indicator_alert_notification.models import IndicatorAlertNotificationSummaryV447

def test_v447_summary():
    s = IndicatorAlertNotificationSummaryV447()
    assert s.ready is True
    assert s.indicator_name == "yasara"
    assert s.live_execution_enabled is False
