class StrategyAllocationSafetyPolicy:
    def policy(self):
        return {"ready": True, "allocation_only": True, "real_execution_enabled": False, "broker_connection_enabled": False, "auto_trading_enabled": False, "requires_risk_gate": True, "requires_human_confirmation": True, "execution_allowed": False}
    def can_allocate_real_capital(self):
        return {"ready": True, "allowed": False, "reason": "real_capital_allocation_disabled"}
strategy_allocation_safety_policy = StrategyAllocationSafetyPolicy()
