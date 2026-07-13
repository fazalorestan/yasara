from fastapi import APIRouter
from app.final_package_v1.package_summary import FinalPackageSummaryBuilderV1
from app.final_package_v1.package_assembly import PackageAssemblyPlanBuilderV1
from app.final_package_v1.final_export_gate import FinalExportGateBuilderV1

router = APIRouter(prefix="/final-package-v1", tags=["final-package-v1"])

@router.get("/summary")
async def summary():
    return FinalPackageSummaryBuilderV1().build()

@router.get("/assembly-plan")
async def assembly_plan():
    return PackageAssemblyPlanBuilderV1().build()

@router.get("/export-gate")
async def export_gate():
    return FinalExportGateBuilderV1().build()
