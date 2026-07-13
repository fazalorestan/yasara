from app.platform_core.api_health.catalog import APIEndpointCatalog
from app.platform_core.api_health.router_visibility import APIRouterVisibilityChecker

def test_v500_alpha17_1_visibility_full_passes():
    expected = [item["path"] for item in APIEndpointCatalog().endpoints()]
    result = APIRouterVisibilityChecker().check(routes=expected)
    assert result["ready"] is True
    assert result["available_count"] == len(expected)
