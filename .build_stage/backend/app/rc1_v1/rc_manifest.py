from datetime import datetime, timezone
from pydantic import BaseModel, Field

class RCManifestV1(BaseModel):
    product: str = "YaSara"
    edition: str = "Professional"
    version: str = "1.0.0-rc1"
    minimum_tests_required: int = 217
    generated_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))

class RCManifestBuilderV1:
    def build(self) -> RCManifestV1:
        return RCManifestV1()
