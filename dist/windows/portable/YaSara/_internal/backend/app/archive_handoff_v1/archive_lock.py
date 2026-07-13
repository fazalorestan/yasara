from datetime import datetime, timezone
from pydantic import BaseModel, Field

class ArchiveLockV1(BaseModel):
    locked: bool = True
    archive_name: str = "yasara_professional_v1_0_stable"
    version: str = "1.0.0"
    locked_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))

class ArchiveLockBuilderV1:
    def build(self) -> ArchiveLockV1:
        return ArchiveLockV1()
