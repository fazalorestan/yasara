from datetime import datetime, timezone
from pydantic import BaseModel, Field

class BackupPlanV1(BaseModel):
    backup_id: str
    paths: list[str] = Field(default_factory=list)
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))

class BackupManagerV1:
    def plan_before_upgrade(self, version: str) -> BackupPlanV1:
        return BackupPlanV1(backup_id=f"pre_upgrade_{version}", paths=["data", "backend/.env", "docs"])
