class ExecutionLifecycleSafetyPolicy:
    def policy(self):
        return {
            "ready": True,
            "lifecycle_tracking_only": True,
            "real_execution_enabled": False,
            "real_fill_enabled": False,
            "broker_connection_enabled": False,
            "auto_trading_enabled": False,
            "execution_allowed": False,
        }

    def can_record_real_fill(self):
        return {"ready": True, "allowed": False, "reason": "real_fill_recording_disabled"}

execution_lifecycle_safety_policy = ExecutionLifecycleSafetyPolicy()
