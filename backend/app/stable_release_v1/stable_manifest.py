from datetime import datetime, timezone
from pydantic import BaseModel, Field

class StableReleaseManifestV1(BaseModel):
    product: str = "YaSara"
    edition: str = "Professional"
    version: str = "1.0.0"
    channel: str = "stable"
    minimum_tests_required: int = 242
    release_name: str = "YaSara Professional v1.0 Stable"
    generated_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))

class StableReleaseManifestBuilderV1:
    def build(self) -> StableReleaseManifestV1:
        return StableReleaseManifestV1()
