class BrokerSafetyPolicy:
    def policy(self):
        return {"ready": True, "live_execution_allowed": False, "auto_trading_allowed": False, "requires_license": True, "requires_risk_approval": True, "requires_execution_guard": True, "requires_user_confirmation": True, "mode": "contract_only"}
broker_safety_policy = BrokerSafetyPolicy()
