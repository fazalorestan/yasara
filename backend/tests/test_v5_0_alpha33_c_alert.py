from app.platform_core.ai_decision.integration.alert_link import AIDecisionAlertLink

def test_v500_alpha33_c_alert(): assert AIDecisionAlertLink().alert_contract()['delivery_enabled'] is False