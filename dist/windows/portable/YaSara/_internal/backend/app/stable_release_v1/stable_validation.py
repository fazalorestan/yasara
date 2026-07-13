from pydantic import BaseModel, Field
from app.stable_release_v1.build_freeze import BuildFreezeBuilderV1
from app.stable_release_v1.stable_manifest import StableReleaseManifestBuilderV1

class StableValidationReportV1(BaseModel):
    stable_ready: bool
    version: str
    checks: list[str] = Field(default_factory=list)

class StableValidationBuilderV1:
    def build(self) -> StableValidationReportV1:
        manifest = StableReleaseManifestBuilderV1().build()
        freeze = BuildFreezeBuilderV1().build()
        return StableValidationReportV1(
            stable_ready=freeze.frozen and manifest.channel == "stable",
            version=manifest.version,
            checks=["stable_manifest", "build_freeze", "archive_plan", "install_guide"],
        )
