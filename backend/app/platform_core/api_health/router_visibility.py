from app.platform_core.api_health.catalog import api_endpoint_catalog

class APIRouterVisibilityChecker:
    def check(self, routes: list[str] | None = None):
        expected = [item["path"] for item in api_endpoint_catalog.endpoints()]
        # None means static self-check with expected routes.
        # [] means explicit empty route list.
        available = set(expected if routes is None else routes)
        missing = [path for path in expected if path not in available]
        return {
            "ready": len(missing) == 0,
            "expected_count": len(expected),
            "available_count": len(available),
            "missing": missing,
        }

api_router_visibility_checker = APIRouterVisibilityChecker()
