from datetime import datetime, timezone
from pydantic import BaseModel, Field

class AuditEventV1(BaseModel):
    event_id: str
    actor: str = "system"
    action: str
    target: str
    metadata: dict = Field(default_factory=dict)
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))

class AuditTrailV1:
    def __init__(self):
        self.events: list[AuditEventV1] = []

    def record(self, event: AuditEventV1) -> AuditEventV1:
        self.events.append(event)
        return event

    def list_by_action(self, action: str) -> list[AuditEventV1]:
        return [e for e in self.events if e.action == action]
