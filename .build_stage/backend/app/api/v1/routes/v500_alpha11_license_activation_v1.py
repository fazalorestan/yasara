from fastapi import APIRouter
from app.v500_alpha11_license_activation.service import LicenseActivationFacadeV500Alpha11

router = APIRouter(prefix="/v5-0-alpha-11/license-activation", tags=["v5.0-alpha.11-license-activation"])
_service = LicenseActivationFacadeV500Alpha11()

@router.get("/summary")
async def summary():
    return _service.summary()

@router.get("/fingerprint")
async def fingerprint(seed: str = "local-device"):
    return _service.fingerprint(seed)

@router.get("/activate-demo")
async def activate_demo():
    return _service.activate_demo()

@router.get("/activation-status")
async def activation_status():
    return _service.activation_status()

@router.get("/slots")
async def slots(license_type: str = "demo"):
    return _service.slots(license_type)

@router.get("/revoke-plan")
async def revoke_plan(license_key: str = "DEMO-YASARA-TRIAL"):
    return _service.revoke_plan(license_key)

@router.get("/contract")
async def contract():
    return _service.contract()
