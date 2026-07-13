from pydantic import BaseModel

class IndicatorSettingsPresetsSummaryV448(BaseModel):
    ready: bool = True
    phase: str = "v4_48_yasara_indicator_settings_presets_contract"
    scope: str = "indicator_settings_presets"
    indicator_name: str = "yasara"
    no_new_trading_features: bool = True
    live_execution_enabled: bool = False
    backward_compatible: bool = True
    safety: str = "settings_presets_contract_only_no_real_execution"
