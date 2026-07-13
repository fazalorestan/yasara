from pydantic import BaseModel, Field
from time import time


class CleanupRuleV11(BaseModel):
    pattern: str
    action: str = "delete"
    safe: bool = True
    reason: str = ""


class OperationsHealthCheckV11(BaseModel):
    key: str
    passed: bool
    message: str = ""


class OperationsHealthReportV11(BaseModel):
    ready: bool
    checks: list[OperationsHealthCheckV11] = Field(default_factory=list)


class ProjectInfoV11(BaseModel):
    product: str = "YaSara Professional"
    version: str = "1.1.0-phase5"
    safety: str = "live_trading_disabled"
    modules: list[str] = Field(default_factory=list)
    timestamp: float = Field(default_factory=time)


class ReleaseVerificationV11(BaseModel):
    ready: bool
    required_files: list[str] = Field(default_factory=list)
    missing_files: list[str] = Field(default_factory=list)
