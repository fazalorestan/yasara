from pydantic import BaseModel, Field
from app.v11_alerts.service import AlertsNotificationServiceV11


class V11Phase8Summary(BaseModel):
    ready: bool
    phase: str = "v1_1_phase_8_alerts_notification_engine"
    capabilities: list[str] = Field(default_factory=list)
    safety: str = "notifications_only_no_trade_execution"


class V11Phase8SummaryBuilder:
    def build(self) -> V11Phase8Summary:
        snapshot = AlertsNotificationServiceV11().demo()
        return V11Phase8Summary(
            ready=snapshot.ready and len(snapshot.events) >= 2 and len(snapshot.deliveries) >= 2,
            capabilities=[
                "alert_rules",
                "price_alerts",
                "risk_alerts",
                "ai_signal_alerts",
                "notification_center",
                "dashboard_notifications",
                "alerts_snapshot_api",
            ],
        )
