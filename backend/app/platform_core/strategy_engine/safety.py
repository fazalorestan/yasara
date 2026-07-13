class StrategySafetyPolicy:
    def policy(self):
        return {
            "ready": True,
            "real_execution_enabled": False,
            "auto_trading_enabled": False,
            "requires_risk_gate": True,
            "requires_human_confirmation": True,
            "advisory_only": True,
            "execution_allowed": False,
        }

    def can_execute(self):
        return {"ready": True, "allowed": False, "reason": "strategy_execution_disabled"}

strategy_safety_policy = StrategySafetyPolicy()
