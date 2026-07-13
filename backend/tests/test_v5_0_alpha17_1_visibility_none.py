from app.platform_core.api_health.router_visibility import APIRouterVisibilityChecker

def test_v500_alpha17_1_visibility_none_uses_expected_catalog():
    result = APIRouterVisibilityChecker().check(routes=None)
    assert result["ready"] is True
    assert result["missing"] == []
