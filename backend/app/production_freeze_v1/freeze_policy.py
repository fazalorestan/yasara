from pydantic import BaseModel, Field

class FreezeRuleV1(BaseModel):
    key: str
    allowed: bool
    note: str = ""

class ProductionFreezePolicyV1(BaseModel):
    frozen: bool = True
    rules: list[FreezeRuleV1] = Field(default_factory=list)

class ProductionFreezePolicyBuilderV1:
    def build(self) -> ProductionFreezePolicyV1:
        return ProductionFreezePolicyV1(rules=[
            FreezeRuleV1(key="feature_changes", allowed=False, note="Only critical hotfixes after final freeze"),
            FreezeRuleV1(key="documentation_fixes", allowed=True),
            FreezeRuleV1(key="security_hotfixes", allowed=True),
            FreezeRuleV1(key="live_trading_enablement", allowed=False, note="Reserved for v1.1 safety-gated release"),
        ])
