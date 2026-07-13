from fastapi import APIRouter
from app.archive_handoff_v1.archive_lock import ArchiveLockBuilderV1
from app.archive_handoff_v1.handoff_manifest import HandoffManifestBuilderV1
from app.archive_handoff_v1.stable_delivery_lock import StableDeliveryLockBuilderV1
from app.archive_handoff_v1.project_done_summary import ProjectDoneSummaryBuilderV1

router = APIRouter(prefix="/archive-handoff-v1", tags=["archive-handoff-v1"])

@router.get("/archive-lock")
async def archive_lock():
    return ArchiveLockBuilderV1().build()

@router.get("/handoff-manifest")
async def handoff_manifest():
    return HandoffManifestBuilderV1().build()

@router.get("/delivery-lock")
async def delivery_lock():
    return StableDeliveryLockBuilderV1().build()

@router.get("/done")
async def done():
    return ProjectDoneSummaryBuilderV1().build()
