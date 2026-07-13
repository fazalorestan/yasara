class BrokerMonitoringSafetyPolicy:
    def policy(self):
        return {
            "ready": True,
            "monitoring_only": True,
            "real_broker_connection_enabled": False,
            "real_account_read_enabled": False,
            "real_order_submit_enabled": False,
            "real_execution_enabled": False,
            "auto_trading_enabled": False,
            "execution_allowed": False,
        }

    def can_probe_real_broker(self):
        return {"ready": True, "allowed": False, "reason": "real_broker_probe_disabled"}

broker_monitoring_safety_policy = BrokerMonitoringSafetyPolicy()
