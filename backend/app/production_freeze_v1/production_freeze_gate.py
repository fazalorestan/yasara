from pydantic import BaseModel, Field
from app.production_freeze_v1.freeze_policy import ProductionFreezePolicyBuilderV1
from app.production_freeze_v1.safety_assertions import ProductionSafetyAssertionsBuilderV1
from app.production_freeze_v1.version_registry import VersionRegistryBuilderV1

class ProductionFreezeGateV1(BaseModel):
    passed: bool
    checks: list[str] = Field(default_factory=list)

class ProductionFreezeGateBuilderV1:
    def build(self) -> ProductionFreezeGateV1:
        policy = ProductionFreezePolicyBuilderV1().build()
        safety = ProductionSafetyAssertionsBuilderV1().build()
        registry = VersionRegistryBuilderV1().build()
        return ProductionFreezeGateV1(
            passed=policy.frozen and safety.passed and any(e.version == "1.0.0" and e.status == "ready" for e in registry.entries),
            checks=["freeze_policy", "safety_assertions", "version_registry"],
        )
