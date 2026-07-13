from pydantic import BaseModel, Field
from app.rc1_v1.rc_manifest import RCManifestBuilderV1
from app.rc1_v1.regression_plan import RegressionPlanBuilderV1
from app.rc1_v1.security_gate import SecurityGateBuilderV1

class RC1SummaryV1(BaseModel):
    ready: bool
    version: str
    checks: list[str] = Field(default_factory=list)

class RC1SummaryBuilderV1:
    def build(self) -> RC1SummaryV1:
        manifest = RCManifestBuilderV1().build()
        regression = RegressionPlanBuilderV1().build()
        security = SecurityGateBuilderV1().build()
        return RC1SummaryV1(
            ready=bool(regression.suites and security.passed),
            version=manifest.version,
            checks=["regression_plan", "security_gate", "rc_manifest"],
        )
