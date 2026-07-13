from pydantic import BaseModel, Field

class SyncItemV1(BaseModel):
    item_id: str
    status: str
    payload: dict = Field(default_factory=dict)

class SyncResultV1(BaseModel):
    synced: int
    missing: int
    conflicts: int

class OrderPositionSynchronizerV1:
    def compare(self, local: list[SyncItemV1], remote: list[SyncItemV1]) -> SyncResultV1:
        local_ids = {i.item_id for i in local}
        remote_ids = {i.item_id for i in remote}
        synced = len(local_ids & remote_ids)
        missing = len(remote_ids - local_ids)
        conflicts = len([i for i in local if i.item_id in remote_ids and i.status == "conflict"])
        return SyncResultV1(synced=synced, missing=missing, conflicts=conflicts)
