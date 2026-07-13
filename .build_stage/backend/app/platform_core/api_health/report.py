from app.platform_core.api_health.runner import api_smoke_test_runner
from app.platform_core.api_health.router_visibility import api_router_visibility_checker

class APIHealthReportBuilder:
    def build(self):
        smoke = api_smoke_test_runner.run_static()
        visibility = api_router_visibility_checker.check()
        return {
            "ready": smoke["ready"] and visibility["ready"],
            "smoke": smoke,
            "visibility": visibility,
            "recommendation": "restart_backend_if_new_routes_return_not_found",
            "execution_allowed": False,
        }

api_health_report_builder = APIHealthReportBuilder()
