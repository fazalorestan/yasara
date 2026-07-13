from enum import StrEnum
from pydantic import BaseModel

class NotificationChannel(StrEnum):
    IN_APP = "in_app"
    TELEGRAM = "telegram"
    EMAIL = "email"

class NotificationRuleV1(BaseModel):
    rule_id: str
    event_type: str
    channel: NotificationChannel = NotificationChannel.IN_APP
    enabled: bool = True

class NotificationRuleEngineV1:
    def route(self, rules: list[NotificationRuleV1], event_type: str) -> list[NotificationRuleV1]:
        return [r for r in rules if r.enabled and r.event_type == event_type]
