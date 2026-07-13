from app.platform_core.ai_decision.health import AIDecisionHealthService

def test_v500_alpha33_b_health_execution(): assert AIDecisionHealthService().health()['execution_allowed'] is False
