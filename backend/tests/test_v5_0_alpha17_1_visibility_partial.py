from app.platform_core.api_health.catalog import APIEndpointCatalog
from app.platform_core.api_health.router_visibility import APIRouterVisibilityChecker

def test_v500_alpha17_1_visibility_partial_detects_missing_routes():
    expected = [item["path"] for item in APIEndpointCatalog().endpoints()]
    result = APIRouterVisibilityChecker().check(routes=expected[:1])
    assert result["ready"] is False
    assert len(result["missing"]) == len(expected) - 1
