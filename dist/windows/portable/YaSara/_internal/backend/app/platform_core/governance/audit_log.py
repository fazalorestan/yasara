from dataclasses import dataclass, field
from typing import Any
from app.platform_core.clock import utc_now_iso

@dataclass
class AuditRecord:
    action: str
    actor: str = "system"
    payload: dict[str, Any] = field(default_factory=dict)
    ts: str = field(default_factory=utc_now_iso)

class AuditLog:
    def __init__(self):
        self._records: list[AuditRecord] = []

    def write(self, action: str, actor: str = "system", payload: dict | None = None):
        record = AuditRecord(action=action, actor=actor, payload=payload or {})
        self._records.append(record)
        return record

    def list(self, limit: int = 100):
        return [r.__dict__ for r in self._records[-limit:]]

audit_log = AuditLog()
