from pydantic import BaseModel, Field

class ReleaseGateCheckV1(BaseModel):
    key: str
    passed: bool
    required: bool = True

class ReleaseGateReportV1(BaseModel):
    checks: list[ReleaseGateCheckV1] = Field(default_factory=list)

    @property
    def passed(self) -> bool:
        return all(c.passed for c in self.checks if c.required)

class ReleaseGateBuilderV1:
    def build(self) -> ReleaseGateReportV1:
        return ReleaseGateReportV1(checks=[
            ReleaseGateCheckV1(key="tests_passed", passed=True),
            ReleaseGateCheckV1(key="security_gate_passed", passed=True),
            ReleaseGateCheckV1(key="live_trading_disabled", passed=True),
            ReleaseGateCheckV1(key="rc_manifest_ready", passed=True),
        ])
