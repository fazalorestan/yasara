from pydantic import BaseModel, Field
from app.consolidation_v1.archive_plan import ArchivePlanBuilderV1
from app.consolidation_v1.package_manifest import FinalPackageManifestBuilderV1
from app.consolidation_v1.release_tree import ReleaseTreePlanBuilderV1
from app.consolidation_v1.size_report import ProjectSizeReportBuilderV1

class ConsolidationPhaseBReadinessV1(BaseModel):
    ready: bool
    checks: list[str] = Field(default_factory=list)

class ConsolidationPhaseBReadinessBuilderV1:
    def build(self) -> ConsolidationPhaseBReadinessV1:
        archive = ArchivePlanBuilderV1().build()
        package = FinalPackageManifestBuilderV1().build()
        tree = ReleaseTreePlanBuilderV1().build()
        size = ProjectSizeReportBuilderV1().build_static_policy()
        return ConsolidationPhaseBReadinessV1(
            ready=bool(archive.targets and package.sections and tree.nodes and size.items),
            checks=["archive_plan", "package_manifest", "release_tree", "size_policy"],
        )
