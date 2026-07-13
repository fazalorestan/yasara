from pydantic import BaseModel, Field
from app.final_integration_v1.final_app_structure import FinalAppStructureBuilderV1
from app.final_integration_v1.final_release_tree import FinalReleaseTreeBuilderV1
from app.final_integration_v1.module_merge_map import ModuleMergeMapBuilderV1
from app.final_integration_v1.transient_file_policy import TransientFilePolicyBuilderV1

class FinalIntegrationPhase1ReadinessV1(BaseModel):
    ready: bool
    checks: list[str] = Field(default_factory=list)
    note: str = "This phase prepares consolidation but does not move/delete files automatically."

class FinalIntegrationPhase1ReadinessBuilderV1:
    def build(self) -> FinalIntegrationPhase1ReadinessV1:
        merge = ModuleMergeMapBuilderV1().build()
        structure = FinalAppStructureBuilderV1().build()
        tree = FinalReleaseTreeBuilderV1().build()
        policy = TransientFilePolicyBuilderV1().build()
        return FinalIntegrationPhase1ReadinessV1(
            ready=bool(merge.targets and structure.packages and tree.items and policy.rules),
            checks=["module_merge_map", "final_app_structure", "release_tree", "transient_policy"],
        )
