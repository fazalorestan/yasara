class BrokerReconnectPolicy:
    def policy(self):
        return {"ready": True, "max_retries": 3, "backoff": "linear", "simulated_only": True, "real_connection": False, "execution_allowed": False}
    def attempt(self, retry_count: int):
        allowed = retry_count < self.policy()["max_retries"]
        return {"ready": True, "retry_count": retry_count, "retry_allowed": allowed, "next_state": "connecting" if allowed else "failed", "execution_allowed": False}
broker_reconnect_policy = BrokerReconnectPolicy()
