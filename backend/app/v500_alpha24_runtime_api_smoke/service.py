from app.platform_core.runtime_api_smoke.service import runtime_api_smoke_service
from app.v500_alpha24_runtime_api_smoke.models import RuntimeAPISmokeSummaryV500Alpha24

class RuntimeAPISmokeFacadeV500Alpha24:
    def summary(self): return RuntimeAPISmokeSummaryV500Alpha24()
    def catalog(self): return runtime_api_smoke_service.catalog()
    def plan(self): return runtime_api_smoke_service.plan()
    def audit(self): return runtime_api_smoke_service.audit()
    def runner(self): return runtime_api_smoke_service.runner()
    def validate_status(self): return runtime_api_smoke_service.validate_status(200)
    def validate_payload(self): return runtime_api_smoke_service.validate_payload_ok()
    def readiness(self): return runtime_api_smoke_service.readiness()
    def contract(self):
        return {
            "ready": True,
            "purpose": "detect_missing_routers_before_manual_api_testing",
            "future_live_http_runner": True,
            "execution_allowed": False,
        }
