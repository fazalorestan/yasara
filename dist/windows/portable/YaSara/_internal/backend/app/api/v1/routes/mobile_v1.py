from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from app.mobile_v1.application.service import mobile_service_v1
from app.mobile_v1.domain.models import MobileDevice, MobilePushMessage, MobileSettings

router = APIRouter(prefix="/mobile-v1", tags=["mobile-v1"])

class OwnerRequest(BaseModel):
    owner_id: str = "default"

class PushRequest(BaseModel):
    device_id: str
    message: MobilePushMessage

@router.post("/devices")
async def register_device(device: MobileDevice):
    return await mobile_service_v1.register_device(device)

@router.get("/devices")
async def list_devices(owner_id: str = "default"):
    return await mobile_service_v1.list_devices(owner_id)

@router.delete("/devices/{device_id}")
async def disable_device(device_id: str):
    result = await mobile_service_v1.disable_device(device_id)
    if result is None:
        raise HTTPException(status_code=404, detail="Device not found")
    return result

@router.get("/settings")
async def get_settings(owner_id: str = "default"):
    return await mobile_service_v1.get_settings(owner_id)

@router.put("/settings")
async def save_settings(settings: MobileSettings):
    return await mobile_service_v1.save_settings(settings)

@router.get("/home")
async def home(owner_id: str = "default"):
    return await mobile_service_v1.home(owner_id)

@router.get("/offline-sync")
async def offline_sync(owner_id: str = "default"):
    return await mobile_service_v1.offline_sync(owner_id)

@router.post("/push")
async def push(payload: PushRequest):
    result = await mobile_service_v1.send_push(payload.device_id, payload.message)
    if result is None:
        raise HTTPException(status_code=404, detail="Device not found")
    return result
