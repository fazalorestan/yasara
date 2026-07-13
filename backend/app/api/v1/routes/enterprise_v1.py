from fastapi import APIRouter
from app.enterprise_v1.enterprise_summary import EnterpriseSummaryBuilderV1
from app.enterprise_v1.startup_validation import StartupValidatorV1
from app.enterprise_v1.module_discovery import ModuleDiscoveryV1

router = APIRouter(prefix="/enterprise-v1", tags=["enterprise-v1"])

@router.get("/summary")
async def summary():
    return EnterpriseSummaryBuilderV1().build()

@router.get("/startup-validation")
async def startup_validation():
    return StartupValidatorV1().validate()

@router.get("/modules")
async def modules():
    return ModuleDiscoveryV1().discover_static()
