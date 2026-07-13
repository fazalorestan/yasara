from datetime import datetime, timedelta, timezone
from pydantic import BaseModel, Field

class CacheEntryV1(BaseModel):
    key: str
    value: object
    expires_at: datetime

    @property
    def expired(self) -> bool:
        return datetime.now(timezone.utc) >= self.expires_at

class MarketDataCacheV1:
    def __init__(self, ttl_seconds: int = 10):
        self.ttl_seconds = ttl_seconds
        self._items: dict[str, CacheEntryV1] = {}

    def set(self, key: str, value: object) -> object:
        self._items[key] = CacheEntryV1(
            key=key,
            value=value,
            expires_at=datetime.now(timezone.utc) + timedelta(seconds=self.ttl_seconds),
        )
        return value

    def get(self, key: str):
        entry = self._items.get(key)
        if entry is None:
            return None
        if entry.expired:
            self._items.pop(key, None)
            return None
        return entry.value

    def clear(self) -> None:
        self._items.clear()

    def size(self) -> int:
        return len(self._items)
