from app.platform_core.alert_engine.service import AlertEngineFoundationService

def test_v500_alpha28_service_risk_alert(): assert AlertEngineFoundationService().sample_risk_alert()['severity'] == 'critical'
