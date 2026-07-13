from datetime import datetime, timezone
from pydantic import BaseModel, Field

class FinalReleaseManifestV1(BaseModel):
    product: str = "YaSara"
    edition: str = "Professional"
    version: str = "1.0.0"
    channel: str = "stable-candidate"
    minimum_tests_required: int = 235
    live_trading_enabled_by_default: bool = False
    telemetry_enabled_by_default: bool = False
    generated_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))

class FinalReleaseManifestBuilderV1:
    def build(self) -> FinalReleaseManifestV1:
        return FinalReleaseManifestV1()
