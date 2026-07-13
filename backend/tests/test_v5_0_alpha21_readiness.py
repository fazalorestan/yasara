from app.platform_core.patching.readiness import PatchPipelineReadinessGate

def test_v500_alpha21_readiness():
    r=PatchPipelineReadinessGate().run(); assert r['ready'] is True; assert r['checks']['destructive_actions_allowed'] is False
