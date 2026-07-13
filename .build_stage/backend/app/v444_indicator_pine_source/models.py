from pydantic import BaseModel

class IndicatorPineSourceSummaryV444(BaseModel):
    ready: bool = True
    phase: str = "v4_44_yasara_indicator_pine_source_archive"
    scope: str = "indicator_source_management"
    indicator_name: str = "yasara"
    source_language: str = "pine_script_v6"
    no_new_trading_features: bool = True
    live_execution_enabled: bool = False
    backward_compatible: bool = True
    safety: str = "source_archive_only_no_real_execution"
