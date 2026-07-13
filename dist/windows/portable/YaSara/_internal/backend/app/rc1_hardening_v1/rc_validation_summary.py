from pydantic import BaseModel, Field
from app.rc1_hardening_v1.release_gate import ReleaseGateBuilderV1
from app.rc1_hardening_v1.runtime_smoke import RuntimeSmokePlannerV1
from app.rc1_hardening_v1.api_contract import APIContractBuilderV1

class RCHardeningSummaryV1(BaseModel):
    ready: bool
    checks: list[str] = Field(default_factory=list)
    next_step: str = "final_release_candidate"

class RCHardeningSummaryBuilderV1:
    def build(self) -> RCHardeningSummaryV1:
        gate = ReleaseGateBuilderV1().build()
        smoke = RuntimeSmokePlannerV1().build()
        api = APIContractBuilderV1().build()
        return RCHardeningSummaryV1(
            ready=gate.passed and bool(smoke.checks) and bool(api.endpoints),
            checks=["runtime_smoke", "api_contract", "release_gate"],
        )
