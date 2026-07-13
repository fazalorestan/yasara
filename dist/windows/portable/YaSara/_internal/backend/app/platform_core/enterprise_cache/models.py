from dataclasses import dataclass, field
from typing import Any
from app.platform_core.clock import utc_now_iso

@dataclass
class CacheEntry:
    key: str
    value: Any
    ttl_seconds: int = 300
    created_at: str = field(default_factory=utc_now_iso)
    hits: int = 0

@dataclass
class CachePolicy:
    name: str
    ttl_seconds: int = 300
    max_items: int = 10000
    mode: str = "memory"

@dataclass
class RedisAdapterContract:
    enabled: bool = False
    host_ref: str = "REDIS_HOST"
    port_ref: str = "REDIS_PORT"
    mode: str = "contract_only"
