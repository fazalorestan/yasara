from app.platform_core.api_routing.planner import router_registration_planner
from app.platform_core.api_routing.swagger import swagger_visibility_contract

class AutoRouterHealthReport:
    def report(self):
        plan = router_registration_planner.build_plan()
        swagger = swagger_visibility_contract.expected_visibility()
        return {
            "ready": plan["ready"] and swagger["ready"],
            "plan": plan,
            "swagger": swagger,
            "manual_router_patch_required": False,
            "execution_allowed": False,
        }

auto_router_health_report = AutoRouterHealthReport()
