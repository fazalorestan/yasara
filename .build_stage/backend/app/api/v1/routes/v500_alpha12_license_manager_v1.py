from fastapi import APIRouter
from app.v500_alpha12_license_manager.service import LicenseManagerFacadeV500Alpha12

router = APIRouter(prefix="/v5-0-alpha-12/license-manager", tags=["v5.0-alpha.12-license-manager"])
_service = LicenseManagerFacadeV500Alpha12()

@router.get("/summary")
async def summary():
    return _service.summary()

@router.get("/status")
async def status(license_type: str = "demo"):
    return _service.status(license_type)

@router.get("/plan")
async def plan(license_type: str = "demo", days: int = 30):
    return _service.plan(license_type, days)

@router.get("/admin-operations")
async def admin_operations():
    return _service.admin_operations()

@router.get("/demo-renewal-policy")
async def demo_renewal_policy():
    return _service.demo_renewal_policy()

@router.get("/can-renew-demo")
async def can_renew_demo(previous_renewals: int = 0):
    return _service.can_renew_demo(previous_renewals)

@router.get("/health")
async def health():
    return _service.health()

@router.get("/export-sample")
async def export_sample(license_type: str = "demo"):
    return _service.export_sample(license_type)

@router.get("/import-sample")
async def import_sample():
    return _service.import_sample()

@router.get("/contract")
async def contract():
    return _service.contract()
