from app.platform_core.alert_engine.readiness import AlertEngineReadinessGate

def test_v500_alpha28_readiness():
    r=AlertEngineReadinessGate().run(); assert r['ready'] is True; assert r['execution_allowed'] is False
