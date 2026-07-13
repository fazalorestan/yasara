from app.platform_core.api_health.service import api_health_framework_service
from app.v500_alpha17_api_health.models import APIHealthSummaryV500Alpha17

class APIHealthFacadeV500Alpha17:
    def summary(self):
        return APIHealthSummaryV500Alpha17()

    def catalog(self):
        return api_health_framework_service.catalog()

    def smoke(self):
        return api_health_framework_service.smoke()

    def visibility(self):
        return api_health_framework_service.visibility()

    def report(self):
        return api_health_framework_service.report()

    def readiness(self):
        return api_health_framework_service.readiness()

    def contract(self):
        return {
            "ready": True,
            "checks": ["endpoint_catalog", "status_200", "json_shape", "ready_field", "router_visibility", "health_report"],
            "manual_api_test_url": "http://127.0.0.1:8000/docs",
            "execution_allowed": False,
        }
