class BrokerOrderRoutingSafetyPolicy:
    def policy(self):
        return {"ready": True, "paper_routing_only": True, "real_broker_connection_enabled": False, "real_order_submit_enabled": False, "real_execution_enabled": False, "auto_trading_enabled": False, "execution_allowed": False}
    def can_submit_real_order(self):
        return {"ready": True, "allowed": False, "reason": "real_broker_order_submit_disabled"}
broker_order_routing_safety_policy = BrokerOrderRoutingSafetyPolicy()
