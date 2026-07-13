class OrderRoutingSafetyPolicy:
    def policy(self):
        return {
            "ready": True,
            "routing_only": True,
            "dry_route_only": True,
            "real_execution_enabled": False,
            "broker_connection_enabled": False,
            "auto_trading_enabled": False,
            "execution_allowed": False,
        }

    def can_route_to_real_broker(self):
        return {"ready": True, "allowed": False, "reason": "real_broker_routing_disabled"}

order_routing_safety_policy = OrderRoutingSafetyPolicy()
