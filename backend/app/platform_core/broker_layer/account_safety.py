class BrokerAccountSafetyPolicy:
    def policy(self):
        return {"ready": True, "real_account_read_enabled": False, "real_balance_read_enabled": False, "real_position_read_enabled": False, "real_broker_connection_enabled": False, "real_execution_enabled": False, "auto_trading_enabled": False, "execution_allowed": False}
    def can_read_real_account(self):
        return {"ready": True, "allowed": False, "reason": "real_account_read_disabled"}
broker_account_safety_policy = BrokerAccountSafetyPolicy()
