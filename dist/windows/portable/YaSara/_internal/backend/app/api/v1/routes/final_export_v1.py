from fastapi import APIRouter
from app.final_export_v1.final_delivery_summary import FinalDeliverySummaryBuilderV1
from app.final_export_v1.export_manifest import FinalExportManifestBuilderV1
from app.final_export_v1.handoff_checklist import FinalHandoffChecklistBuilderV1
from app.final_export_v1.version_seal import VersionSealBuilderV1

router = APIRouter(prefix="/final-export-v1", tags=["final-export-v1"])

@router.get("/summary")
async def summary():
    return FinalDeliverySummaryBuilderV1().build()

@router.get("/manifest")
async def manifest():
    return FinalExportManifestBuilderV1().build()

@router.get("/handoff-checklist")
async def handoff_checklist():
    return FinalHandoffChecklistBuilderV1().build()

@router.get("/version-seal")
async def version_seal():
    return VersionSealBuilderV1().build()
