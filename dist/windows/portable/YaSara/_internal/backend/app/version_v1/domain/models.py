from datetime import datetime, timezone
from enum import StrEnum
from pydantic import BaseModel, Field

class ReleaseChannel(StrEnum):
    DEV = "dev"
    BETA = "beta"
    RC = "rc"
    STABLE = "stable"

class ReleaseComponentStatus(StrEnum):
    READY = "ready"
    WARNING = "warning"
    BLOCKED = "blocked"

class ReleaseComponent(BaseModel):
    name: str
    version: str
    status: ReleaseComponentStatus
    notes: str = ""

class VersionInfo(BaseModel):
    product: str = "YaSara"
    version: str = "1.0.0"
    channel: ReleaseChannel = ReleaseChannel.STABLE
    build: str = "stable-production"
    api_version: str = "v1"
    generated_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))

class ReleaseManifest(BaseModel):
    version: VersionInfo
    components: list[ReleaseComponent] = Field(default_factory=list)
    checksums: dict[str, str] = Field(default_factory=dict)
    release_notes: list[str] = Field(default_factory=list)

class FinalVerificationResult(BaseModel):
    ready: bool
    total_checks: int
    passed_checks: int
    warnings: list[str] = Field(default_factory=list)
    blockers: list[str] = Field(default_factory=list)
    manifest: ReleaseManifest
    generated_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
