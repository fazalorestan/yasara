from fastapi import APIRouter
from app.v448_indicator_settings_presets.service import IndicatorSettingsPresetsFacadeV448

router = APIRouter(prefix="/v4-48/indicator-settings-presets", tags=["v4.48-indicator-settings-presets"])
_service = IndicatorSettingsPresetsFacadeV448()

@router.get("/summary")
async def summary():
    return _service.summary()

@router.get("/presets")
async def presets():
    return _service.presets()

@router.get("/preset")
async def preset(name: str = "default"):
    return _service.preset(name)

@router.post("/validate")
async def validate(settings: dict | None = None):
    return _service.validate(settings)

@router.post("/apply-override")
async def apply_override(preset: str = "default", overrides: dict | None = None):
    return _service.apply_override(preset, overrides)

@router.get("/versions")
async def versions():
    return _service.versions()
