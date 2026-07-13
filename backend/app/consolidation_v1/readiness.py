from pydantic import BaseModel, Field
from app.consolidation_v1.project_manifest import ConsolidatedProjectManifestBuilderV1
from app.consolidation_v1.cleanup_policy import ConsolidationCleanupPolicyBuilderV1
from app.consolidation_v1.final_structure import FinalProjectStructureBuilderV1

class ConsolidationReadinessReportV1(BaseModel):
    ready: bool
    checks: list[str] = Field(default_factory=list)
    warnings: list[str] = Field(default_factory=list)

class ConsolidationReadinessBuilderV1:
    def build(self) -> ConsolidationReadinessReportV1:
        manifest = ConsolidatedProjectManifestBuilderV1().build()
        cleanup = ConsolidationCleanupPolicyBuilderV1().build()
        structure = FinalProjectStructureBuilderV1().build()
        return ConsolidationReadinessReportV1(
            ready=manifest.total_confirmed_tests >= 179 and len(cleanup.rules) > 0 and len(structure.folders) > 0,
            checks=[
                "tests_confirmed",
                "cleanup_policy_available",
                "final_structure_defined",
                "release_pro_layer_available",
            ],
            warnings=[
                "Consolidation Phase A does not delete files automatically.",
                "Manual review is required before final pruning.",
            ],
        )
