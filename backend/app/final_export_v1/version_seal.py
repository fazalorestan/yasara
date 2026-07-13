from datetime import datetime, timezone
from pydantic import BaseModel, Field

class VersionSealV1(BaseModel):
    version: str = "1.0.0"
    sealed: bool = True
    seal_note: str = "YaSara Professional v1.0 Stable"
    sealed_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))

class VersionSealBuilderV1:
    def build(self) -> VersionSealV1:
        return VersionSealV1()
