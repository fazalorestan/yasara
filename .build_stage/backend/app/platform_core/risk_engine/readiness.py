from app.platform_core.risk_engine.service import risk_engine_foundation_service

class RiskEngineReadinessGate:
    def run(self):
        policy = risk_engine_foundation_service.policy()
        sizing = risk_engine_foundation_service.position_size()
        preflight = risk_engine_foundation_service.preflight()
        ready = sizing["ready"] and preflight["ready"] and policy["live_execution_allowed"] is False
        return {"ready": ready, "checks": {"policy_ready": True, "position_sizing_ready": sizing["ready"], "preflight_ready": preflight["ready"], "live_execution_allowed": False, "auto_trading_allowed": False}, "execution_allowed": False}

risk_engine_readiness_gate = RiskEngineReadinessGate()
