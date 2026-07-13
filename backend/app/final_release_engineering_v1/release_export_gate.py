from pydantic import BaseModel, Field
from app.final_release_engineering_v1.artifact_manifest import ArtifactManifestBuilderV1
from app.final_release_engineering_v1.checksum_plan import ChecksumPlanBuilderV1
from app.final_release_engineering_v1.portable_export_plan import PortableExportPlanBuilderV1

class ReleaseExportGateV1(BaseModel):
    passed: bool
    checks: list[str] = Field(default_factory=list)

class ReleaseExportGateBuilderV1:
    def build(self) -> ReleaseExportGateV1:
        artifacts = ArtifactManifestBuilderV1().build()
        checksums = ChecksumPlanBuilderV1().build()
        portable = PortableExportPlanBuilderV1().build()
        return ReleaseExportGateV1(
            passed=bool(artifacts.artifacts and checksums.targets and portable.include),
            checks=["artifact_manifest", "checksum_plan", "portable_export_plan"],
        )
