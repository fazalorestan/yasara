class StrategyScoringSafetyPolicy:
    def policy(self):
        return {
            "ready": True,
            "scoring_only": True,
            "real_execution_enabled": False,
            "auto_trading_enabled": False,
            "requires_risk_gate": True,
            "execution_allowed": False,
        }

    def can_emit_executable_signal(self):
        return {"ready": True, "allowed": False, "reason": "executable_signals_disabled"}

strategy_scoring_safety_policy = StrategyScoringSafetyPolicy()
