from enum import StrEnum
from pydantic import BaseModel

class ConflictStrategy(StrEnum):
    LOCAL_WINS = "local_wins"
    REMOTE_WINS = "remote_wins"

class SyncConflictV1(BaseModel):
    key: str
    local: dict
    remote: dict

class SyncConflictResolverV1:
    def resolve(self, conflict: SyncConflictV1, strategy: ConflictStrategy) -> dict:
        return conflict.local if strategy == ConflictStrategy.LOCAL_WINS else conflict.remote
