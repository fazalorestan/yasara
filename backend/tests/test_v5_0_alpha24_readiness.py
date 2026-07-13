from app.platform_core.runtime_api_smoke.readiness import RuntimeAPISmokeReadinessGate

def test_v500_alpha24_readiness():
    r=RuntimeAPISmokeReadinessGate().run(); assert r['ready'] is True; assert r['score'] == 100.0
