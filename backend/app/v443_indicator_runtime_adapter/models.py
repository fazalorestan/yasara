from pydantic import BaseModel

class IndicatorRuntimeAdapterSummaryV443(BaseModel):
    ready: bool = True
    phase: str = "v4_43_yasara_indicator_runtime_adapter"
    scope: str = "indicator_runtime_adapter"
    indicator_name: str = "yasara"
    runtime_version: str = "v1.0"
    no_new_trading_features: bool = True
    live_execution_enabled: bool = False
    backward_compatible: bool = True
    safety: str = "analysis_runtime_only_no_real_execution"
