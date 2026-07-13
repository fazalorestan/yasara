from pydantic import BaseModel, Field
from app.final_integration_v1.phase1_readiness import FinalIntegrationPhase1ReadinessBuilderV1

class FinalIntegrationPhase1SummaryV1(BaseModel):
    ready: bool
    previous_confirmed_tests: int = 248
    next_phase: str = "release_engineering"
    checks: list[str] = Field(default_factory=list)

class FinalIntegrationPhase1SummaryBuilderV1:
    def build(self) -> FinalIntegrationPhase1SummaryV1:
        readiness = FinalIntegrationPhase1ReadinessBuilderV1().build()
        return FinalIntegrationPhase1SummaryV1(
            ready=readiness.ready,
            checks=readiness.checks,
        )
