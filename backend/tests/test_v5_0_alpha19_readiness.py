from app.platform_core.api_routing.readiness import AutoRouterReadinessGate

def test_v500_alpha19_readiness():
    r=AutoRouterReadinessGate().run(); assert 'score' in r; assert r['execution_allowed'] is False
