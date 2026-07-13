from pydantic import BaseModel
class IndicatorExpansionSummaryV500Alpha1(BaseModel):
    ready: bool = True
    phase: str = "v5_0_alpha_1_indicator_expansion_foundation"
    default_indicator: str = "yasara"
    no_new_trading_features: bool = True
    live_execution_enabled: bool = False
    backward_compatible: bool = True
