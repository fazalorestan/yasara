class BrokerExecutionSafetyContract:
    def policy(self):
        return {
            "ready": True,
            "real_execution_enabled": False,
            "auto_trading_enabled": False,
            "requires_risk_engine": True,
            "requires_human_confirmation": True,
            "dry_run_only": True,
            "execution_allowed": False,
        }

    def can_execute(self):
        return {"ready": True, "allowed": False, "reason": "real_execution_disabled"}

broker_execution_safety_contract = BrokerExecutionSafetyContract()
