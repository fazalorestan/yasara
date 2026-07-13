from app.platform_core.api_search.readiness import LauncherSwaggerSearchReadinessGate

def test_v500_alpha20_readiness():
    r=LauncherSwaggerSearchReadinessGate().run(); assert r['ready'] is True; assert r['score'] == 100.0
