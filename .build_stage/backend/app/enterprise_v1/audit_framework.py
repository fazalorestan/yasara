from datetime import datetime, timezone
from pydantic import BaseModel, Field

class EnterpriseAuditRecordV1(BaseModel):
    actor: str
    action: str
    resource: str
    metadata: dict = Field(default_factory=dict)
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))

class EnterpriseAuditFrameworkV1:
    def record(self, actor: str, action: str, resource: str) -> EnterpriseAuditRecordV1:
        return EnterpriseAuditRecordV1(actor=actor, action=action, resource=resource)
