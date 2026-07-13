from dataclasses import dataclass, field
from typing import Any
from app.platform_core.clock import utc_now_iso

@dataclass
class LicensePayload:
    license_key: str
    license_type: str = "demo"
    owner: str = "trial-user"
    issued_at: str = field(default_factory=utc_now_iso)
    expires_at: str | None = None
    features: list[str] = field(default_factory=list)
    device_limit: int = 1
    workspace_limit: int = 1
    alert_limit: int = 10
    metadata: dict[str, Any] = field(default_factory=dict)

@dataclass
class LicenseValidationResult:
    valid: bool
    license_type: str = "unknown"
    features: list[str] = field(default_factory=list)
    errors: list[str] = field(default_factory=list)
    warnings: list[str] = field(default_factory=list)

@dataclass
class FeatureEntitlement:
    feature: str
    enabled: bool
    reason: str = ""
