from fastapi import APIRouter
from app.v500_alpha13_license_ui.service import LicenseUIFacadeV500Alpha13

router = APIRouter(prefix="/v5-0-alpha-13/license-ui", tags=["v5.0-alpha.13-license-ui"])
_service = LicenseUIFacadeV500Alpha13()

@router.get("/summary")
async def summary():
    return _service.summary()

@router.get("/status-card")
async def status_card(license_type: str = "demo"):
    return _service.status_card(license_type)

@router.get("/countdown")
async def countdown():
    return _service.countdown()

@router.get("/feature-locks")
async def feature_locks(license_type: str = "demo"):
    return _service.feature_locks(license_type)

@router.get("/upgrade-prompt")
async def upgrade_prompt(feature: str = "ADVANCED_AI"):
    return _service.upgrade_prompt(feature)

@router.get("/settings-page")
async def settings_page():
    return _service.settings_page()

@router.get("/admin-panel")
async def admin_panel():
    return _service.admin_panel()

@router.get("/full-contract")
async def full_contract(license_type: str = "demo"):
    return _service.full_contract(license_type)
