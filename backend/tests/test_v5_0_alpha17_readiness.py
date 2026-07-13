from app.platform_core.api_health.readiness import APISmokeReadinessGate

def test_v500_alpha17_readiness():
    r = APISmokeReadinessGate().run()
    assert r['ready'] is True
    assert r['score'] == 100.0
