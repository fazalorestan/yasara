from app.platform_core.patching.self_healing.readiness import SelfHealingPatchReadinessGate

def test_v500_alpha25_readiness(): assert 'score' in SelfHealingPatchReadinessGate().run()
