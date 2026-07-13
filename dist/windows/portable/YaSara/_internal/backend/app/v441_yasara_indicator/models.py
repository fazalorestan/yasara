from pydantic import BaseModel

class YaSaraIndicatorSummaryV441(BaseModel):
    ready: bool = True
    phase: str = "v4_41_yasara_indicator_plugin_foundation"
    scope: str = "indicator_plugin_foundation"
    indicator_name: str = "yasara"
    enabled_by_default: bool = True
    no_new_trading_features: bool = True
    live_execution_enabled: bool = False
    backward_compatible: bool = True
    safety: str = "analysis_indicator_only_no_real_execution"
