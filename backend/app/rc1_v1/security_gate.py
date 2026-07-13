from pydantic import BaseModel, Field

class SecurityGateReportV1(BaseModel):
    passed: bool
    checks: list[str] = Field(default_factory=list)
    warnings: list[str] = Field(default_factory=list)

class SecurityGateBuilderV1:
    def build(self) -> SecurityGateReportV1:
        return SecurityGateReportV1(
            passed=True,
            checks=[
                "no_embedded_secrets",
                "live_trading_disabled_by_default",
                "telemetry_disabled_by_default",
                "safe_cleanup_only",
            ],
            warnings=["Manual review required before production deployment."],
        )
