from pydantic import BaseModel, Field
from app.final_release_v1.distribution_checklist import DistributionChecklistBuilderV1
from app.final_release_v1.final_manifest import FinalReleaseManifestBuilderV1

class FinalQAGateV1(BaseModel):
    passed: bool
    version: str
    checks: list[str] = Field(default_factory=list)

class FinalQAGateBuilderV1:
    def build(self) -> FinalQAGateV1:
        manifest = FinalReleaseManifestBuilderV1().build()
        distribution = DistributionChecklistBuilderV1().build()
        return FinalQAGateV1(
            passed=distribution.ready and not manifest.live_trading_enabled_by_default and not manifest.telemetry_enabled_by_default,
            version=manifest.version,
            checks=["distribution_ready", "live_trading_disabled", "telemetry_disabled", "manifest_ready"],
        )
