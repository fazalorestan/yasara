from pydantic import BaseModel, Field
from app.final_package_v1.final_export_gate import FinalExportGateBuilderV1

class FinalPackageSummaryV1(BaseModel):
    ready: bool
    previous_confirmed_tests: int = 284
    package_name: str = "YaSara Professional v1.0"
    next_step: str = "manual_zip_export"
    checks: list[str] = Field(default_factory=list)

class FinalPackageSummaryBuilderV1:
    def build(self) -> FinalPackageSummaryV1:
        gate = FinalExportGateBuilderV1().build()
        return FinalPackageSummaryV1(ready=gate.passed, checks=gate.checks)
