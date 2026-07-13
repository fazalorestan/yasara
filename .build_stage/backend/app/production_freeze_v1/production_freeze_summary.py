from pydantic import BaseModel, Field
from app.production_freeze_v1.production_freeze_gate import ProductionFreezeGateBuilderV1

class ProductionFreezeSummaryV1(BaseModel):
    ready: bool
    version: str = "1.0.0"
    message: str = "YaSara Professional v1.0 production freeze is ready."
    checks: list[str] = Field(default_factory=list)

class ProductionFreezeSummaryBuilderV1:
    def build(self) -> ProductionFreezeSummaryV1:
        gate = ProductionFreezeGateBuilderV1().build()
        return ProductionFreezeSummaryV1(ready=gate.passed, checks=gate.checks)
