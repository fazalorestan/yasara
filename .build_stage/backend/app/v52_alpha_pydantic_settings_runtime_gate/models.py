from pydantic import BaseModel
class PydanticSettingsRuntimeGateSummaryV52Alpha(BaseModel):
    ready: bool = True
    phase: str = 'v5_2_alpha_package_o'
    build_id: str = '2026.52.O.001'
    pydantic_settings_gate: bool = True
    executable_validation: bool = True
    signal_only_default: bool = True
    auto_trading_enabled: bool = False
    test_pack_size: int = 90
