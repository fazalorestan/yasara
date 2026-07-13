from datetime import datetime, timezone
from pydantic import BaseModel, Field

class CloudAuditEventV1(BaseModel):
    event_id: str
    user_id: str
    action: str
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))

class CloudAuditLogV1:
    def __init__(self):
        self.events: list[CloudAuditEventV1] = []

    def record(self, event: CloudAuditEventV1):
        self.events.append(event)
        return event

    def by_user(self, user_id: str):
        return [e for e in self.events if e.user_id == user_id]
