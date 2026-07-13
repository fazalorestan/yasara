from pydantic import BaseModel
from datetime import datetime, timezone

class NotificationViewItemV1(BaseModel):
    title: str
    body: str
    severity: str = "info"
    created_at: datetime = datetime.now(timezone.utc)

class NotificationCenterViewV1:
    def unread_count(self, items: list[NotificationViewItemV1]) -> int:
        return len(items)

    def critical(self, items: list[NotificationViewItemV1]) -> list[NotificationViewItemV1]:
        return [i for i in items if i.severity == "critical"]
