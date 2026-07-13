from pydantic import BaseModel

class IndicatorEngineBridgeSummaryV445(BaseModel):
    ready: bool = True
    phase: str = "v4_45_yasara_indicator_engine_bridge"
    scope: str = "indicator_engine_bridge"
    indicator_name: str = "yasara"
    no_new_trading_features: bool = True
    live_execution_enabled: bool = False
    backward_compatible: bool = True
    safety: str = "analysis_bridge_only_no_real_execution"
