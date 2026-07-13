from pydantic import BaseModel, Field
from time import time


class FinalReleaseArtifactV11(BaseModel):
    name: str
    path: str
    required: bool = True


class FinalReleaseCheckV11(BaseModel):
    key: str
    passed: bool
    message: str = ""


class FinalReleaseManifestV11(BaseModel):
    product: str = "YaSara Professional"
    version: str = "1.1.0"
    status: str = "final"
    previous_version: str = "1.0.0"
    live_trading_enabled: bool = False
    telemetry_enabled: bool = False
    created_at: float = Field(default_factory=time)
    artifacts: list[FinalReleaseArtifactV11] = Field(default_factory=list)
    checks: list[FinalReleaseCheckV11] = Field(default_factory=list)


class FinalReleaseSummaryV11(BaseModel):
    ready: bool
    progress_percent: int = 100
    version: str = "1.1.0"
    checks_passed: int
    checks_total: int
    safety: str = "final_release_live_trading_disabled"
