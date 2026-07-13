from datetime import datetime, timezone
from pydantic import BaseModel, Field

class BackupManifestV1(BaseModel):
    backup_id: str
    owner_id: str
    sections: list[str] = Field(default_factory=list)
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))

class BackupManifestBuilderV1:
    def build(self, owner_id: str, sections: list[str]) -> BackupManifestV1:
        return BackupManifestV1(backup_id=f"backup_{owner_id}", owner_id=owner_id, sections=sections)
