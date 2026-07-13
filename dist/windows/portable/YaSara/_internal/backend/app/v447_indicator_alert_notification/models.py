from pydantic import BaseModel

class IndicatorAlertNotificationSummaryV447(BaseModel):
    ready: bool = True
    phase: str = "v4_47_yasara_indicator_alert_notification_contract"
    scope: str = "indicator_alert_notification"
    indicator_name: str = "yasara"
    no_new_trading_features: bool = True
    live_execution_enabled: bool = False
    backward_compatible: bool = True
    safety: str = "alert_notification_contract_only_no_real_execution"
