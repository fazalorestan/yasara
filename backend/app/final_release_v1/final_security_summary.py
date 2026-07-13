from pydantic import BaseModel, Field

class FinalSecuritySummaryV1(BaseModel):
    passed: bool = True
    controls: list[str] = Field(default_factory=list)
    warnings: list[str] = Field(default_factory=list)

class FinalSecuritySummaryBuilderV1:
    def build(self) -> FinalSecuritySummaryV1:
        return FinalSecuritySummaryV1(
            controls=[
                "no_embedded_secrets",
                "live_trading_disabled_by_default",
                "telemetry_disabled_by_default",
                "dry_run_private_api",
                "safe_cleanup_policy",
            ],
            warnings=["Manual production secret configuration required before any live deployment."],
        )
