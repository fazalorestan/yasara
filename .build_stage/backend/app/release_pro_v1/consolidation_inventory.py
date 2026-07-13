from pydantic import BaseModel, Field

class ConsolidationModuleV1(BaseModel):
    name: str
    category: str
    keep: bool = True

class ConsolidationInventoryV1(BaseModel):
    modules: list[ConsolidationModuleV1] = Field(default_factory=list)

class ConsolidationInventoryBuilderV1:
    def build(self) -> ConsolidationInventoryV1:
        names = [
            ("multi_exchange_v1", "exchange"),
            ("market_tools_v1", "market"),
            ("connectivity_v1", "connectivity"),
            ("ai_trading_v1", "ai"),
            ("desktop_ui_v1", "ui"),
            ("cloud_v1", "cloud"),
        ]
        return ConsolidationInventoryV1(modules=[ConsolidationModuleV1(name=n, category=c) for n, c in names])
