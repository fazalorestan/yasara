from app.platform_core.api_health.router_visibility import APIRouterVisibilityChecker

def test_v500_alpha17_1_visibility_empty_means_no_routes_available():
    result = APIRouterVisibilityChecker().check(routes=[])
    assert result["ready"] is False
    assert result["available_count"] == 0
    assert len(result["missing"]) == result["expected_count"]
