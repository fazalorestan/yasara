from pydantic import BaseModel, Field
from app.archive_handoff_v1.archive_lock import ArchiveLockBuilderV1
from app.archive_handoff_v1.handoff_manifest import HandoffManifestBuilderV1

class StableDeliveryLockV1(BaseModel):
    ready: bool
    version: str
    checks: list[str] = Field(default_factory=list)

class StableDeliveryLockBuilderV1:
    def build(self) -> StableDeliveryLockV1:
        archive = ArchiveLockBuilderV1().build()
        manifest = HandoffManifestBuilderV1().build()
        return StableDeliveryLockV1(
            ready=archive.locked and bool(manifest.items),
            version=archive.version,
            checks=["archive_lock", "handoff_manifest", "stable_delivery"],
        )
