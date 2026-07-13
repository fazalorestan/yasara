from pydantic import BaseModel, Field

class SafetyAssertionV1(BaseModel):
    key: str
    passed: bool = True

class ProductionSafetyAssertionsV1(BaseModel):
    assertions: list[SafetyAssertionV1] = Field(default_factory=list)

    @property
    def passed(self) -> bool:
        return all(a.passed for a in self.assertions)

class ProductionSafetyAssertionsBuilderV1:
    def build(self) -> ProductionSafetyAssertionsV1:
        return ProductionSafetyAssertionsV1(assertions=[
            SafetyAssertionV1(key="live_trading_disabled_by_default"),
            SafetyAssertionV1(key="telemetry_disabled_by_default"),
            SafetyAssertionV1(key="no_embedded_api_keys"),
            SafetyAssertionV1(key="dry_run_private_orders"),
            SafetyAssertionV1(key="safe_cleanup_scripts_only"),
        ])
