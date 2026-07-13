from pydantic import BaseModel

class IndicatorSandboxSummaryV500Alpha3(BaseModel):
    ready: bool = True
    phase: str = "v5_0_alpha_3_indicator_sandbox_validation"
    scope: str = "indicator_sandbox_validation_foundation"
    no_new_trading_features: bool = True
    live_execution_enabled: bool = False
    backward_compatible: bool = True
