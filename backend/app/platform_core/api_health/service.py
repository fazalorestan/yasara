from app.platform_core.api_health.catalog import api_endpoint_catalog
from app.platform_core.api_health.readiness import api_smoke_readiness_gate
from app.platform_core.api_health.report import api_health_report_builder
from app.platform_core.api_health.router_visibility import api_router_visibility_checker
from app.platform_core.api_health.runner import api_smoke_test_runner

class APIHealthFrameworkService:
    def catalog(self):
        return {"ready": True, "endpoints": api_endpoint_catalog.endpoints()}

    def smoke(self):
        return api_smoke_test_runner.run_static()

    def visibility(self):
        return api_router_visibility_checker.check()

    def report(self):
        return api_health_report_builder.build()

    def readiness(self):
        return api_smoke_readiness_gate.run()

api_health_framework_service = APIHealthFrameworkService()
