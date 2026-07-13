from fastapi import APIRouter
from app.v500_alpha10_license_enforcement.service import LicenseEnforcementFacadeV500Alpha10

router = APIRouter(prefix="/v5-0-alpha-10/license-enforcement", tags=["v5.0-alpha.10-license-enforcement"])
_service = LicenseEnforcementFacadeV500Alpha10()

@router.get("/summary")
async def summary():
    return _service.summary()

@router.get("/check-feature")
async def check_feature(feature: str = "BASIC_ANALYSIS", license_type: str = "demo"):
    return _service.check_feature(feature, license_type)

@router.get("/flags")
async def flags(license_type: str = "demo"):
    return _service.flags(license_type)

@router.get("/check-plugin")
async def check_plugin(plugin: str = "yasara_indicator", license_type: str = "demo"):
    return _service.check_plugin(plugin, license_type)

@router.get("/demo-usage")
async def demo_usage(alerts: int = 0, indicators: int = 1, workspaces: int = 1):
    return _service.demo_usage(alerts, indicators, workspaces)

@router.get("/usage")
async def usage():
    return _service.usage()

@router.get("/contract")
async def contract():
    return _service.contract()
