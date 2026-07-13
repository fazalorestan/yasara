from datetime import datetime, timezone
from enum import StrEnum
from pydantic import BaseModel, Field

class ReleaseCheckStatus(StrEnum):
    PASS = "pass"
    WARN = "warn"
    FAIL = "fail"

class DeploymentEnvironment(StrEnum):
    LOCAL = "local"
    STAGING = "staging"
    PRODUCTION = "production"

class ReleaseCheck(BaseModel):
    key: str
    title: str
    status: ReleaseCheckStatus
    message: str
    required: bool = True

class ReleaseReadinessReport(BaseModel):
    version: str = "sprint18"
    environment: DeploymentEnvironment = DeploymentEnvironment.LOCAL
    ready: bool
    checks: list[ReleaseCheck] = Field(default_factory=list)
    generated_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))

class BackupPlan(BaseModel):
    database: str = "postgresql"
    include_logs: bool = True
    include_uploads: bool = True
    destination: str = "./backups"
    retention_days: int = 14

class BackupResult(BaseModel):
    accepted: bool
    dry_run: bool = True
    backup_id: str
    plan: BackupPlan
    message: str
    generated_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))

class LoadTestScenario(BaseModel):
    name: str
    users: int = 10
    duration_seconds: int = 60
    endpoint: str = "/health"
    method: str = "GET"

class LoadTestPlan(BaseModel):
    scenarios: list[LoadTestScenario] = Field(default_factory=list)
    generated_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
