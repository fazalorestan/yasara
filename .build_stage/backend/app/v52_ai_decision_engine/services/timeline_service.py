from collections import deque
from threading import RLock
import time

class TimelineService:
    def __init__(self):
        self._items = deque(maxlen=500)
        self._lock = RLock()
    def append(self, result):
        item = {
            "timestamp": time.time(),
            "symbol": result.symbol,
            "timeframe": result.timeframe,
            "decision": result.decision.value,
            "confidence": result.confidence,
            "quality_score": result.quality_score,
        }
        with self._lock:
            self._items.appendleft(item)
        return item
    def list(self, limit=100):
        with self._lock:
            return list(self._items)[:limit]
