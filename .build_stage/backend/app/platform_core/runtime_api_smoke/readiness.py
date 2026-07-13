from app.platform_core.runtime_api_smoke.plan import runtime_api_smoke_plan
from app.platform_core.runtime_api_smoke.router_audit import router_registration_audit
from app.platform_core.runtime_api_smoke.runner_contract import runtime_api_smoke_runner_contract

class RuntimeAPISmokeReadinessGate:
    def run(self):
        plan = runtime_api_smoke_plan.build()
        audit = router_registration_audit.audit()
        runner = runtime_api_smoke_runner_contract.static_run()
        ready = plan["ready"] and audit["ready"] and runner["ready"]
        return {
            "ready": ready,
            "score": 100.0 if ready else 0.0,
            "plan": plan,
            "audit": audit,
            "runner": runner,
            "execution_allowed": False,
        }

runtime_api_smoke_readiness_gate = RuntimeAPISmokeReadinessGate()
