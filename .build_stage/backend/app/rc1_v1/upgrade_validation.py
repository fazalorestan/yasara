from pydantic import BaseModel, Field

class UpgradeValidationPlanV1(BaseModel):
    from_version: str = "1.0.0-pro"
    to_version: str = "1.0.0-rc1"
    checks: list[str] = Field(default_factory=list)

class UpgradeValidationPlannerV1:
    def build(self) -> UpgradeValidationPlanV1:
        return UpgradeValidationPlanV1(checks=[
            "backup_created",
            "migration_plan_available",
            "config_preserved",
            "smoke_tests_after_upgrade",
        ])
