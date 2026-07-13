from app.platform_core.api_routing.discovery import auto_router_discovery
from app.platform_core.api_routing.health import auto_router_health_report
from app.platform_core.api_routing.planner import router_registration_planner
from app.platform_core.api_routing.readiness import auto_router_readiness_gate
from app.platform_core.api_routing.registration import safe_router_registrar
from app.platform_core.api_routing.swagger import swagger_visibility_contract

class AutoRouterDiscoveryService:
    def discover(self):
        return {"ready": True, "modules": auto_router_discovery.discover_modules()}

    def plan(self):
        return router_registration_planner.build_plan()

    def dry_run(self):
        return safe_router_registrar.dry_run(auto_router_discovery.discover_modules())

    def swagger(self):
        return swagger_visibility_contract.expected_visibility()

    def health(self):
        return auto_router_health_report.report()

    def readiness(self):
        return auto_router_readiness_gate.run()

auto_router_discovery_service = AutoRouterDiscoveryService()
