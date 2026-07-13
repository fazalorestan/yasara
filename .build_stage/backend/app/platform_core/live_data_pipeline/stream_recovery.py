class LiveStreamRecoveryPolicy:
    def policy(self):
        return {"ready": True, "max_retries": 3, "backoff": "linear", "cooldown_ms": 1000, "simulated_only": True}
    def attempt(self, retry_count: int):
        allowed = retry_count < self.policy()["max_retries"]
        return {"ready": True, "retry_count": retry_count, "retry_allowed": allowed, "next_state": "recovering" if allowed else "failed"}
live_stream_recovery_policy = LiveStreamRecoveryPolicy()
