from pydantic import BaseModel, Field

class RecoveryStepV1(BaseModel):
    order: int
    action: str

class RecoveryPlanV1(BaseModel):
    scenario: str
    steps: list[RecoveryStepV1] = Field(default_factory=list)

class RecoveryPlanBuilderV1:
    def backend_failure(self) -> RecoveryPlanV1:
        return RecoveryPlanV1(scenario="backend_failure", steps=[
            RecoveryStepV1(order=1, action="stop_backend"),
            RecoveryStepV1(order=2, action="inspect_logs"),
            RecoveryStepV1(order=3, action="restore_last_known_config"),
            RecoveryStepV1(order=4, action="restart_backend"),
            RecoveryStepV1(order=5, action="run_smoke_tests"),
        ])
