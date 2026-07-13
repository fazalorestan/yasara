from pydantic import BaseModel, Field

class RollbackValidationPlanV1(BaseModel):
    target_version: str = "1.0.0-pro"
    checks: list[str] = Field(default_factory=list)

class RollbackValidationPlannerV1:
    def build(self) -> RollbackValidationPlanV1:
        return RollbackValidationPlanV1(checks=[
            "restore_backup",
            "restore_config",
            "restart_backend",
            "health_check_after_rollback",
        ])
