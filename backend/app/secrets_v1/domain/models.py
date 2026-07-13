from datetime import datetime, timezone
from enum import StrEnum
from pydantic import BaseModel, Field

class SecretStatus(StrEnum):
    ACTIVE = "active"
    DISABLED = "disabled"
    ROTATED = "rotated"

class SecretScope(StrEnum):
    EXCHANGE = "exchange"
    NOTIFICATION = "notification"
    SYSTEM = "system"

class SecretRecord(BaseModel):
    secret_id: str
    owner_id: str = "default"
    scope: SecretScope
    name: str
    encrypted_value: str
    status: SecretStatus = SecretStatus.ACTIVE
    metadata: dict = Field(default_factory=dict)
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    updated_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))

class SecretCreateRequest(BaseModel):
    owner_id: str = "default"
    scope: SecretScope
    name: str
    value: str
    metadata: dict = Field(default_factory=dict)

class SecretPublicView(BaseModel):
    secret_id: str
    owner_id: str
    scope: SecretScope
    name: str
    status: SecretStatus
    metadata: dict = Field(default_factory=dict)
    created_at: datetime
    updated_at: datetime
