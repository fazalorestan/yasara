from pydantic import BaseModel

class IndicatorChartIntegrationSummaryV442(BaseModel):
    ready: bool = True
    phase: str = "v4_42_yasara_indicator_chart_integration_contract"
    scope: str = "indicator_chart_integration"
    default_indicator: str = "yasara"
    chart_overlay_enabled: bool = True
    no_new_trading_features: bool = True
    live_execution_enabled: bool = False
    backward_compatible: bool = True
    safety: str = "chart_integration_contract_only_no_real_execution"
