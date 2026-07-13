from app.platform_core.ai_decision.integration.service import AIDecisionIntegrationService

def test_v500_alpha33_c_service_status(): assert AIDecisionIntegrationService().status()['execution_allowed'] is False