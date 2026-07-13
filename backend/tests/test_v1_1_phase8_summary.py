from app.v11_alerts.phase8_summary import V11Phase8SummaryBuilder

def test_v11_phase8_summary():
    summary = V11Phase8SummaryBuilder().build()
    assert summary.ready is True
    assert "notification_center" in summary.capabilities
    assert summary.safety == "notifications_only_no_trade_execution"
