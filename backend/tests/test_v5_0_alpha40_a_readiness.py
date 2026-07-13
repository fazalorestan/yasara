from app.platform_core.ai_intelligence.readiness import AICoreKernelReadinessGate

def test_v500_alpha40_a_readiness(): assert AICoreKernelReadinessGate().run()['ready'] is True
