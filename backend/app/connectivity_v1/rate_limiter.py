from dataclasses import dataclass

@dataclass
class RateLimitDecisionV1:
    allowed: bool
    remaining: int
    reason: str

class TokenBucketRateLimiterV1:
    def __init__(self, capacity: int, refill_per_tick: int = 1):
        self.capacity = capacity
        self.tokens = capacity
        self.refill_per_tick = refill_per_tick

    def allow(self, cost: int = 1) -> RateLimitDecisionV1:
        if cost <= self.tokens:
            self.tokens -= cost
            return RateLimitDecisionV1(True, self.tokens, "allowed")
        return RateLimitDecisionV1(False, self.tokens, "rate_limited")

    def refill(self):
        self.tokens = min(self.capacity, self.tokens + self.refill_per_tick)
        return self.tokens
