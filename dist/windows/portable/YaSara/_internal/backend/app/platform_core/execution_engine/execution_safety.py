class ExecutionSafetyPolicy:
    def policy(self):
        return {
            "ready": True,
            "dry_run_only": True,
            "real_execution_enabled": False,
            "broker_connection_enabled": False,
            "auto_trading_enabled": False,
            "requires_human_confirmation": True,
            "requires_risk_gate": True,
            "execution_allowed": False,
        }

    def can_execute_real_order(self):
        return {"ready": True, "allowed": False, "reason": "real_execution_disabled"}

execution_safety_policy = ExecutionSafetyPolicy()
