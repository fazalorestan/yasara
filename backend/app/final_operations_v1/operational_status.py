from pydantic import BaseModel, Field
from app.final_operations_v1.runbook import OperationalRunbookBuilderV1
from app.final_operations_v1.support_matrix import SupportMatrixBuilderV1

class OperationalStatusV1(BaseModel):
    ready: bool
    status: str = "operational_handoff_ready"
    checks: list[str] = Field(default_factory=list)

class OperationalStatusBuilderV1:
    def build(self) -> OperationalStatusV1:
        runbook = OperationalRunbookBuilderV1().build()
        support = SupportMatrixBuilderV1().build()
        return OperationalStatusV1(
            ready=bool(runbook.steps and support.areas),
            checks=["runbook", "support_matrix", "incident_plan", "troubleshooting"],
        )
