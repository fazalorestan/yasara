import time
from collections import defaultdict

class NotificationRateLimiterV1:
    def __init__(self, max_per_minute: int = 30):
        self.max_per_minute = max_per_minute
        self._events: dict[str, list[float]] = defaultdict(list)

    def allow(self, key: str) -> bool:
        now = time.monotonic()
        window_start = now - 60
        events = [t for t in self._events[key] if t >= window_start]
        self._events[key] = events
        if len(events) >= self.max_per_minute:
            return False
        events.append(now)
        return True
