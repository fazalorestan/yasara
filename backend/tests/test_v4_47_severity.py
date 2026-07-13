from app.platform_core.indicators.alerts.severity import IndicatorAlertSeverity

def test_v447_severity():
    s = IndicatorAlertSeverity()
    assert s.resolve("LONG", 90) == "critical"
    assert s.resolve("SHORT", 70) == "warning"
    assert s.resolve("WAIT", 10) == "silent"
