from app.platform_core.alert_engine.severity import AlertSeverityService

def test_v500_alpha28_severity_invalid(): assert AlertSeverityService().validate('bad')['valid'] is False
