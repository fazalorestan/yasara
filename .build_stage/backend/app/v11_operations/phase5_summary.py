from pydantic import BaseModel, Field
from app.v11_operations.service import OperationsMaintenanceServiceV11


class V11Phase5Summary(BaseModel):
    ready: bool
    phase: str = "v1_1_phase_5_operations_maintenance"
    capabilities: list[str] = Field(default_factory=list)
    safety: str = "maintenance_only_no_trading"


class V11Phase5SummaryBuilder:
    def build(self) -> V11Phase5Summary:
        summary = OperationsMaintenanceServiceV11().summary()
        return V11Phase5Summary(
            ready=summary["cleanup_rules"] >= 5,
            capabilities=[
                "cleanup_project_bat",
                "safe_cleanup_policy",
                "deep_cleanup_policy",
                "project_health_check",
                "project_info",
                "release_verification",
                "operations_api",
            ],
        )
