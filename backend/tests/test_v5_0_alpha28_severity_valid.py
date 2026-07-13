from app.platform_core.alert_engine.severity import AlertSeverityService

def test_v500_alpha28_severity_valid(): assert AlertSeverityService().validate('warning')['valid'] is True
