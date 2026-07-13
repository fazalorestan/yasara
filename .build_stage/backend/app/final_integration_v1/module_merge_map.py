from pydantic import BaseModel, Field

class ModuleMergeTargetV1(BaseModel):
    source_module: str
    final_module: str
    category: str

class ModuleMergeMapV1(BaseModel):
    targets: list[ModuleMergeTargetV1] = Field(default_factory=list)

class ModuleMergeMapBuilderV1:
    def build(self) -> ModuleMergeMapV1:
        return ModuleMergeMapV1(targets=[
            ModuleMergeTargetV1(source_module="multi_exchange_v1", final_module="exchanges", category="core"),
            ModuleMergeTargetV1(source_module="market_tools_v1", final_module="market", category="analysis"),
            ModuleMergeTargetV1(source_module="connectivity_v1", final_module="connectivity", category="runtime"),
            ModuleMergeTargetV1(source_module="ai_trading_v1", final_module="ai", category="intelligence"),
            ModuleMergeTargetV1(source_module="desktop_ui_v1", final_module="desktop", category="ui"),
            ModuleMergeTargetV1(source_module="cloud_v1", final_module="cloud", category="platform"),
            ModuleMergeTargetV1(source_module="enterprise_v1", final_module="enterprise", category="platform"),
            ModuleMergeTargetV1(source_module="production_packaging_v1", final_module="packaging", category="release"),
        ])
