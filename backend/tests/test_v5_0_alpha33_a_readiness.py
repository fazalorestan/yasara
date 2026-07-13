from app.platform_core.ai_decision.readiness import AIDecisionCoreReadinessGate

def test_v500_alpha33_a_readiness(): assert AIDecisionCoreReadinessGate().run()['ready'] is True
