from pydantic import BaseModel, Field
from app.final_export_v1.handoff_checklist import FinalHandoffChecklistBuilderV1
from app.final_export_v1.version_seal import VersionSealBuilderV1

class FinalDeliverySummaryV1(BaseModel):
    ready: bool
    version: str
    release_name: str
    previous_confirmed_tests: int = 272
    next_step: str = "final_manual_package_export"
    checks: list[str] = Field(default_factory=list)

class FinalDeliverySummaryBuilderV1:
    def build(self) -> FinalDeliverySummaryV1:
        checklist = FinalHandoffChecklistBuilderV1().build()
        seal = VersionSealBuilderV1().build()
        return FinalDeliverySummaryV1(
            ready=checklist.ready and seal.sealed,
            version=seal.version,
            release_name=seal.seal_note,
            checks=[c.key for c in checklist.checks],
        )
