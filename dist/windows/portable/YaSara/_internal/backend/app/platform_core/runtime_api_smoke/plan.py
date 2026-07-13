from app.platform_core.runtime_api_smoke.catalog import runtime_endpoint_catalog

class RuntimeAPISmokePlan:
    def build(self):
        endpoints = runtime_endpoint_catalog.endpoints()
        return {
            "ready": True,
            "total": len(endpoints),
            "critical": len([e for e in endpoints if e["critical"]]),
            "endpoints": endpoints,
            "mode": "runtime_smoke_plan",
        }

runtime_api_smoke_plan = RuntimeAPISmokePlan()
