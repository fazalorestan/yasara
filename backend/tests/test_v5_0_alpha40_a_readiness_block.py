from app.platform_core.ai_intelligence.readiness import AICoreKernelReadinessGate

def test_v500_alpha40_a_readiness_block(): assert AICoreKernelReadinessGate().run()['execution_allowed'] is False
