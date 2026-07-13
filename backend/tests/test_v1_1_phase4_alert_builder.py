from app.v11_dashboard_runtime.alert_builder import DashboardAlertBuilderV11

def test_dashboard_alert_builder():
    alerts = DashboardAlertBuilderV11().build()
    assert isinstance(alerts, list)
    assert all(alert.level in {"info", "warning", "critical"} for alert in alerts)
