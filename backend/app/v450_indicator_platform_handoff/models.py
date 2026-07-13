from pydantic import BaseModel

class IndicatorPlatformHandoffSummaryV450(BaseModel):
    ready: bool = True
    phase: str = "v4_50_yasara_indicator_platform_handoff"
    scope: str = "indicator_platform_handoff"
    indicator_name: str = "yasara"
    no_new_trading_features: bool = True
    live_execution_enabled: bool = False
    backward_compatible: bool = True
    safety: str = "handoff_only_no_real_execution"
