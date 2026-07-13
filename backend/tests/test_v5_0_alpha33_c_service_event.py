from app.platform_core.ai_decision.integration.service import AIDecisionIntegrationService

def test_v500_alpha33_c_service_event(): assert AIDecisionIntegrationService().event_bus()['ready'] is True