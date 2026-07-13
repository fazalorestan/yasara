class BrokerSafetyPolicy:
    def policy(self):
        return {
            "ready": True,
            "real_broker_connection_enabled": False,
            "real_execution_enabled": False,
            "account_read_enabled": False,
            "auto_trading_enabled": False,
            "requires_human_confirmation": True,
            "execution_allowed": False,
        }

    def can_connect_real_broker(self):
        return {"ready": True, "allowed": False, "reason": "real_broker_connection_disabled"}

broker_safety_policy = BrokerSafetyPolicy()
