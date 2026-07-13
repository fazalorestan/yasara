from dataclasses import dataclass, field
from typing import Any
from app.platform_core.clock import utc_now_iso

@dataclass
class ConfigProfile:
    name: str
    environment: str = "local"
    values: dict[str, Any] = field(default_factory=dict)
    version: str = "v4.35"
    updated_at: str = field(default_factory=utc_now_iso)

@dataclass
class SecretReference:
    key: str
    provider: str = "env"
    ref: str = ""
    exposed: bool = False

@dataclass
class ConfigValidationResult:
    valid: bool
    errors: list[str] = field(default_factory=list)
    warnings: list[str] = field(default_factory=list)
