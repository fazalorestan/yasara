from app.platform_core.api_health.router_visibility import APIRouterVisibilityChecker

def test_v500_alpha17_visibility_missing():
    assert APIRouterVisibilityChecker().check(routes=[])['ready'] is False
