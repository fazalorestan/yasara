from pydantic import BaseModel
class IndicatorMarketplaceSummaryV500Alpha2(BaseModel):
    ready: bool = True
    phase: str = "v5_0_alpha_2_indicator_marketplace_catalog"
    default_indicator: str = "yasara"
    no_new_trading_features: bool = True
    live_execution_enabled: bool = False
    backward_compatible: bool = True
