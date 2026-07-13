from pydantic import BaseModel, Field
from app.final_release_engineering_v1.release_export_gate import ReleaseExportGateBuilderV1

class ReleaseEngineeringSummaryV1(BaseModel):
    ready: bool
    previous_confirmed_tests: int = 256
    next_phase: str = "documentation_and_qa"
    checks: list[str] = Field(default_factory=list)

class ReleaseEngineeringSummaryBuilderV1:
    def build(self) -> ReleaseEngineeringSummaryV1:
        gate = ReleaseExportGateBuilderV1().build()
        return ReleaseEngineeringSummaryV1(ready=gate.passed, checks=gate.checks)
