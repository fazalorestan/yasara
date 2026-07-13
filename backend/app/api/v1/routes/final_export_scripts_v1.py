from fastapi import APIRouter
from app.final_export_scripts_v1.export_status import OneClickExportStatusBuilderV1
from app.final_export_scripts_v1.export_summary import OneClickExportSummaryBuilderV1

router = APIRouter(prefix="/final-export-scripts-v1", tags=["final-export-scripts-v1"])

@router.get("/status")
async def status():
    return OneClickExportStatusBuilderV1().build()

@router.get("/summary")
async def summary():
    return OneClickExportSummaryBuilderV1().build()
