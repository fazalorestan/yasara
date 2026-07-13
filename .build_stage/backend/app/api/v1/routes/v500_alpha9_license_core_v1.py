from fastapi import APIRouter
from app.v500_alpha9_license_core.service import LicenseCoreFacadeV500Alpha9

router = APIRouter(prefix="/v5-0-alpha-9/license-core", tags=["v5.0-alpha.9-license-core"])
_service = LicenseCoreFacadeV500Alpha9()

@router.get("/summary")
async def summary():
    return _service.summary()

@router.get("/trial-policy")
async def trial_policy():
    return _service.trial_policy()

@router.get("/features")
async def features():
    return _service.feature_catalog()

@router.get("/matrix")
async def matrix():
    return _service.matrix()

@router.get("/parse-key")
async def parse_key(key: str = "DEMO-YASARA-TRIAL"):
    return _service.parse_key(key)

@router.get("/create-demo")
async def create_demo():
    return _service.create_demo()

@router.get("/verify-demo")
async def verify_demo():
    return _service.verify_demo()

@router.get("/entitlements")
async def entitlements(license_type: str = "demo"):
    return _service.entitlements(license_type)

@router.get("/can-access")
async def can_access(feature: str = "BASIC_ANALYSIS", license_type: str = "demo"):
    return _service.can_access(feature, license_type)

@router.get("/plugin-requirement")
async def plugin_requirement(plugin: str = "yasara_indicator"):
    return _service.plugin_requirement(plugin)

@router.get("/designer-contract")
async def designer_contract():
    return _service.designer_contract()

@router.get("/contract")
async def contract():
    return _service.contract()
