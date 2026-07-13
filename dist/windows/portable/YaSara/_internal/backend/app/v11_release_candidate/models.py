from pydantic import BaseModel, Field
from time import time


class V11ModuleStatus(BaseModel):
    key: str
    title: str
    ready: bool
    endpoint: str | None = None


class V11IntegrationReport(BaseModel):
    ready: bool
    version: str = "1.1.0-rc1"
    modules: list[V11ModuleStatus] = Field(default_factory=list)
    safety: str = "live_trading_disabled"
    generated_at: float = Field(default_factory=time)


class V11ReleaseChecklistItem(BaseModel):
    key: str
    passed: bool
    message: str = ""


class V11ReleaseCandidateManifest(BaseModel):
    product: str = "YaSara Professional"
    version: str = "1.1.0-rc1"
    status: str = "release_candidate"
    previous_stable: str = "1.0.0"
    live_trading_enabled: bool = False
    checklist: list[V11ReleaseChecklistItem] = Field(default_factory=list)
