from datetime import datetime, timezone
from pydantic import BaseModel, Field

class LogEntryV1(BaseModel):
    level: str
    message: str
    context: dict = Field(default_factory=dict)
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))

class LoggingFrameworkV1:
    def info(self, message: str, context: dict | None = None) -> LogEntryV1:
        return LogEntryV1(level="info", message=message, context=context or {})

    def error(self, message: str, context: dict | None = None) -> LogEntryV1:
        return LogEntryV1(level="error", message=message, context=context or {})
