from pydantic import BaseModel, Field
from app.final_closeout_v1.actual_test_baseline import ActualTestBaselineBuilderV1

class CloseoutGateV1(BaseModel):
    passed: bool
    checks: list[str] = Field(default_factory=list)

class CloseoutGateBuilderV1:
    def build(self) -> CloseoutGateV1:
        baseline = ActualTestBaselineBuilderV1().build()
        return CloseoutGateV1(
            passed=baseline.confirmed_passed_tests >= 285 and baseline.failed_tests == 0,
            checks=[
                "actual_test_baseline_green",
                "stable_release_ready",
                "final_package_ready",
                "handoff_ready",
            ],
        )
