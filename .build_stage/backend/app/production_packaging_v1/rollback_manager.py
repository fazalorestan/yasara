from pydantic import BaseModel, Field

class RollbackPlanV1(BaseModel):
    target_version: str
    actions: list[str] = Field(default_factory=list)

class RollbackManagerV1:
    def plan(self, target_version: str) -> RollbackPlanV1:
        return RollbackPlanV1(target_version=target_version, actions=[
            "stop_services",
            "restore_backup",
            "restore_previous_config",
            "restart_services",
            "run_smoke_tests",
        ])
