from app.platform_core.runtime_api_smoke.catalog import runtime_endpoint_catalog
from app.platform_core.runtime_api_smoke.plan import runtime_api_smoke_plan
from app.platform_core.runtime_api_smoke.readiness import runtime_api_smoke_readiness_gate
from app.platform_core.runtime_api_smoke.router_audit import router_registration_audit
from app.platform_core.runtime_api_smoke.runner_contract import runtime_api_smoke_runner_contract
from app.platform_core.runtime_api_smoke.status_validator import runtime_api_status_validator

class RuntimeAPISmokeService:
    def catalog(self): return {"ready": True, "endpoints": runtime_endpoint_catalog.endpoints()}
    def plan(self): return runtime_api_smoke_plan.build()
    def audit(self): return router_registration_audit.audit()
    def runner(self): return runtime_api_smoke_runner_contract.static_run()
    def validate_status(self, status_code: int = 200): return runtime_api_status_validator.validate_status(status_code)
    def validate_payload_ok(self): return runtime_api_status_validator.validate_payload({"ready": True})
    def readiness(self): return runtime_api_smoke_readiness_gate.run()

runtime_api_smoke_service = RuntimeAPISmokeService()
