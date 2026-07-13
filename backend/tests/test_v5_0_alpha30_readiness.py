from app.platform_core.replay_engine.readiness import ReplayEngineReadinessGate

def test_v500_alpha30_readiness():
    r=ReplayEngineReadinessGate().run(); assert r['ready'] is True; assert r['execution_allowed'] is False
