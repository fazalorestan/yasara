from app.platform_core.ai_decision.integration.service import AIDecisionIntegrationService

def test_v500_alpha33_c_service_context(): assert AIDecisionIntegrationService().context()['symbol']=='BTCUSDT'