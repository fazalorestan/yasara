from time import time
from app.v11_market_data.models import RateLimitRuleV11


class RateLimitManagerV11:
    def __init__(self):
        self.rules: dict[str, RateLimitRuleV11] = {}
        self.calls: dict[str, list[float]] = {}

    def set_rule(self, rule: RateLimitRuleV11) -> None:
        self.rules[rule.exchange.lower()] = rule
        self.calls.setdefault(rule.exchange.lower(), [])

    def allow(self, exchange: str) -> bool:
        key = exchange.lower()
        rule = self.rules.get(key)
        if rule is None:
            return True
        now = time()
        window_start = now - rule.per_seconds
        recent = [t for t in self.calls.get(key, []) if t >= window_start]
        self.calls[key] = recent
        if len(recent) >= rule.max_requests:
            return False
        recent.append(now)
        self.calls[key] = recent
        return True
