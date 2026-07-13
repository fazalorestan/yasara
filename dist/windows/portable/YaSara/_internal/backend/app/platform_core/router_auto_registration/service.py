from app.platform_core.router_auto_registration.audit import router_registration_audit_contract
from app.platform_core.router_auto_registration.discovery import route_module_discovery
from app.platform_core.router_auto_registration.helper import fastapi_router_registration_helper_contract
from app.platform_core.router_auto_registration.importer import route_module_importer
from app.platform_core.router_auto_registration.manifest import router_endpoint_manifest_contract
from app.platform_core.router_auto_registration.planner import router_auto_registration_planner
from app.platform_core.router_auto_registration.readiness import router_auto_registration_readiness_gate

class RouterAutoRegistrationService:
    def discover(self): return {"ready": True, "modules": route_module_discovery.discover()}
    def inspect_sample(self): return route_module_importer.inspect("app.api.v1.routes.v500_alpha30_replay_engine_v1")
    def plan(self): return router_auto_registration_planner.build_plan()
    def helper(self): return fastapi_router_registration_helper_contract.contract()
    def manifest(self): return router_endpoint_manifest_contract.build(router_auto_registration_planner.build_plan()["items"])
    def audit_sample(self): return router_registration_audit_contract.audit_text("api_router.include_router(v500_alpha30_1_router_auto_registration_v1.router)", "v500_alpha30_1_router_auto_registration_v1")
    def readiness(self): return router_auto_registration_readiness_gate.run()

router_auto_registration_service = RouterAutoRegistrationService()
