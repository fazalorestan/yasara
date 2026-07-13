from pydantic import BaseModel, Field
from app.enterprise_v1.startup_validation import StartupValidatorV1

class EnterpriseSummaryV1(BaseModel):
    ready: bool
    modules: list[str] = Field(default_factory=list)
    note: str = "Enterprise foundation scaffold is ready."

class EnterpriseSummaryBuilderV1:
    def build(self) -> EnterpriseSummaryV1:
        report = StartupValidatorV1().validate()
        return EnterpriseSummaryV1(ready=report.valid, modules=report.modules_found)
