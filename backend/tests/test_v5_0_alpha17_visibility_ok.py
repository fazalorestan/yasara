from app.platform_core.api_health.router_visibility import APIRouterVisibilityChecker

def test_v500_alpha17_visibility_ok():
    assert APIRouterVisibilityChecker().check()['ready'] is True
