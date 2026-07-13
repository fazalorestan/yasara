from app.platform_core.router_auto_registration.helper import fastapi_router_registration_helper_contract
from app.platform_core.router_auto_registration.manifest import router_endpoint_manifest_contract
from app.platform_core.router_auto_registration.planner import router_auto_registration_planner

class RouterAutoRegistrationReadinessGate:
    def run(self):
        plan = router_auto_registration_planner.build_plan()
        helper = fastapi_router_registration_helper_contract.contract()
        manifest = router_endpoint_manifest_contract.build(plan["items"])
        ready = helper["ready"] and manifest["ready"]
        return {
            "ready": ready,
            "score": 100.0 if ready else 0.0,
            "plan": plan,
            "helper": helper,
            "manifest": manifest,
            "execution_allowed": False,
        }

router_auto_registration_readiness_gate = RouterAutoRegistrationReadinessGate()
