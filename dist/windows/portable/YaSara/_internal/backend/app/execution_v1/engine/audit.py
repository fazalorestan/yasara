import uuid
from app.execution_v1.domain.models import ExecutionAuditEntry, ExecutionIntent, ExecutionResult

class ExecutionAuditLogV1:
    def __init__(self):
        self.entries: list[ExecutionAuditEntry] = []

    def record(self, event: str, message: str, intent: ExecutionIntent | None = None, result: ExecutionResult | None = None) -> ExecutionAuditEntry:
        entry = ExecutionAuditEntry(
            audit_id=uuid.uuid4().hex,
            event=event,
            message=message,
            intent=intent,
            result=result,
        )
        self.entries.append(entry)
        return entry

    def list_entries(self) -> list[ExecutionAuditEntry]:
        return list(self.entries)
