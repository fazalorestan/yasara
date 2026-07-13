from app.platform_core.diagnostics.models import DiagnosticCheck

class APIHealthAggregator:
    def run(self):
        endpoints = [
            "/api/v1/health",
            "/api/v1/v4-22/platform-core/summary",
            "/api/v1/v4-23/plugin-catalog/summary",
            "/api/v1/v4-24/plugin-registry-sync/summary",
            "/api/v1/v4-25/policy-gate/summary",
            "/api/v1/v4-26/platform-contracts-sdk/summary",
            "/api/v1/v4-27/extension-host/summary",
            "/api/v1/v4-28/plugin-state-snapshot/summary",
            "/api/v1/v4-29/timezone-runtime/summary",
        ]
        return DiagnosticCheck(
            name="api_health_aggregator",
            ready=True,
            severity="info",
            detail="platform API endpoint catalog generated",
            data={"endpoint_count": len(endpoints), "endpoints": endpoints},
        )
