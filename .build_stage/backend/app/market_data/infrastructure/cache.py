import asyncio
import time
from dataclasses import dataclass
from typing import Any

@dataclass
class CacheEntry:
    value: Any
    expires_at: float

class AsyncTTLCache:
    def __init__(self, default_ttl_seconds: int = 60):
        self.default_ttl_seconds = default_ttl_seconds
        self._items: dict[str, CacheEntry] = {}
        self._lock = asyncio.Lock()

    async def get(self, key: str):
        async with self._lock:
            item = self._items.get(key)
            if item is None:
                return None
            if item.expires_at < time.monotonic():
                self._items.pop(key, None)
                return None
            return item.value

    async def set(self, key: str, value, ttl_seconds: int | None = None) -> None:
        async with self._lock:
            self._items[key] = CacheEntry(value=value, expires_at=time.monotonic() + (ttl_seconds or self.default_ttl_seconds))

    async def clear(self) -> None:
        async with self._lock:
            self._items.clear()

    async def stats(self) -> dict:
        async with self._lock:
            now = time.monotonic()
            return {
                "total": len(self._items),
                "active": sum(1 for item in self._items.values() if item.expires_at >= now),
                "expired": sum(1 for item in self._items.values() if item.expires_at < now),
            }
