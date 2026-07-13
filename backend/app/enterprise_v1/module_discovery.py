from pydantic import BaseModel, Field

class DiscoveredModuleV1(BaseModel):
    name: str
    path: str

class ModuleDiscoveryV1:
    def discover_static(self) -> list[DiscoveredModuleV1]:
        return [
            DiscoveredModuleV1(name="multi_exchange_v1", path="app/multi_exchange_v1"),
            DiscoveredModuleV1(name="ai_trading_v1", path="app/ai_trading_v1"),
            DiscoveredModuleV1(name="enterprise_v1", path="app/enterprise_v1"),
        ]
