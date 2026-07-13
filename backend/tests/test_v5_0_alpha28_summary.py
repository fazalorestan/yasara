from app.v500_alpha28_alert_engine.models import AlertEngineSummaryV500Alpha28

def test_v500_alpha28_summary():
    s=AlertEngineSummaryV500Alpha28(); assert s.ready is True; assert s.live_notifications_enabled is False
