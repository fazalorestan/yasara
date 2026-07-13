class RuntimeSafetyPolicy:
    def policy(self):
        return {
            "ready": True,
            "real_execution_enabled": False,
            "real_broker_connection_enabled": False,
            "auto_trading_enabled": False,
            "commercial_execution_engine_enabled": False,
            "commercial_api_key_required": False,
            "backward_compatibility_required": True,
        }

runtime_safety_policy = RuntimeSafetyPolicy()
