class ReconnectPolicyV11:
    def __init__(self, base_delay_seconds: float = 1.0, max_delay_seconds: float = 30.0):
        self.base_delay_seconds = base_delay_seconds
        self.max_delay_seconds = max_delay_seconds

    def delay_for_attempt(self, attempt: int) -> float:
        delay = self.base_delay_seconds * (2 ** max(attempt - 1, 0))
        return min(delay, self.max_delay_seconds)


class ReconnectManagerV11:
    def __init__(self, policy: ReconnectPolicyV11 | None = None):
        self.policy = policy or ReconnectPolicyV11()

    def next_delay(self, attempt: int) -> float:
        return self.policy.delay_for_attempt(attempt)
