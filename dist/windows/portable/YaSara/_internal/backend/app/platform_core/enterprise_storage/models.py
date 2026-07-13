from dataclasses import dataclass, field
from typing import Any
from app.platform_core.clock import utc_now_iso

@dataclass
class StorageRecord:
    key: str
    bucket: str
    payload: dict[str, Any] = field(default_factory=dict)
    created_at: str = field(default_factory=utc_now_iso)

@dataclass
class StoragePolicy:
    bucket: str
    max_items: int = 10000
    retention_days: int = 30
    mode: str = "local"

@dataclass
class ObjectStorageContract:
    enabled: bool = False
    provider: str = "s3_compatible"
    endpoint_ref: str = "OBJECT_STORAGE_ENDPOINT"
    access_key_ref: str = "OBJECT_STORAGE_ACCESS_KEY"
    secret_key_ref: str = "OBJECT_STORAGE_SECRET_KEY"
    mode: str = "contract_only"
