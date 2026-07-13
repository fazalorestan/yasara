from app.platform_core.alert_engine.severity import AlertSeverityService

def test_v500_alpha28_priority(): assert AlertSeverityService().priority('critical') == 3
