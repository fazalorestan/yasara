from pydantic import BaseModel, Field
from app.final_package_v1.checksum_manifest import ChecksumManifestBuilderV1
from app.final_package_v1.docs_bundle_plan import DocsBundlePlanBuilderV1
from app.final_package_v1.package_assembly import PackageAssemblyPlanBuilderV1
from app.final_package_v1.source_bundle_plan import SourceBundlePlanBuilderV1

class FinalExportGateV1(BaseModel):
    passed: bool
    checks: list[str] = Field(default_factory=list)

class FinalExportGateBuilderV1:
    def build(self) -> FinalExportGateV1:
        package = PackageAssemblyPlanBuilderV1().build()
        source = SourceBundlePlanBuilderV1().build()
        docs = DocsBundlePlanBuilderV1().build()
        checksums = ChecksumManifestBuilderV1().build()
        return FinalExportGateV1(
            passed=bool(package.items and source.include and docs.docs and checksums.items),
            checks=["package_assembly", "source_bundle", "docs_bundle", "checksum_manifest"],
        )
