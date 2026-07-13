from fastapi import APIRouter
from pydantic import BaseModel, Field
from app.account_sync_v1.application.service import account_sync_service_v1

router = APIRouter(prefix="/account-sync-v1", tags=["account-sync-v1"])

class OwnerRequest(BaseModel):
    owner_id: str = "default"

class IngestEventRequest(BaseModel):
    owner_id: str = "default"
    payload: dict = Field(default_factory=dict)

class RecoverOrdersRequest(BaseModel):
    owner_id: str = "default"
    local_orders: list[dict] = Field(default_factory=list)

@router.post("/listen-key")
async def create_listen_key(payload: OwnerRequest):
    return await account_sync_service_v1.create_listen_key(payload.owner_id)

@router.post("/listen-key/keepalive")
async def keepalive(payload: OwnerRequest):
    return await account_sync_service_v1.keepalive(payload.owner_id)

@router.post("/stream/connect")
async def connect_stream(payload: OwnerRequest):
    return await account_sync_service_v1.connect_stream(payload.owner_id)

@router.post("/stream/disconnect")
async def disconnect_stream():
    return await account_sync_service_v1.disconnect_stream()

@router.post("/stream/ingest")
async def ingest_event(payload: IngestEventRequest):
    return await account_sync_service_v1.ingest_event(payload.owner_id, payload.payload)

@router.get("/stream/history")
async def stream_history():
    return await account_sync_service_v1.stream_history()

@router.post("/sync")
async def sync_account(payload: OwnerRequest):
    return await account_sync_service_v1.sync_account(payload.owner_id)

@router.post("/orders/recover")
async def recover_orders(payload: RecoverOrdersRequest):
    return await account_sync_service_v1.recover_orders(payload.owner_id, payload.local_orders)
