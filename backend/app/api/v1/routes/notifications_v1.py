from fastapi import APIRouter
from pydantic import BaseModel
from app.notifications_v1.application.service import notification_service_v1
from app.notifications_v1.domain.models import NotificationMessage, NotificationRecipient

router = APIRouter(prefix="/notifications-v1", tags=["notifications-v1"])

class EnqueueRequest(BaseModel):
    message: NotificationMessage
    recipients: list[NotificationRecipient]

class SignalNotificationRequest(BaseModel):
    symbol: str
    direction: str
    confidence: float
    recipients: list[NotificationRecipient]
    reasons: list[str] = []

@router.post("/enqueue")
async def enqueue(payload: EnqueueRequest):
    return await notification_service_v1.enqueue(payload.message, payload.recipients)

@router.post("/process")
async def process_queue():
    return await notification_service_v1.process()

@router.get("/report")
async def delivery_report():
    return await notification_service_v1.report()

@router.get("/history")
async def history():
    return await notification_service_v1.history()

@router.post("/signal")
async def send_signal(payload: SignalNotificationRequest):
    return await notification_service_v1.send_signal(
        symbol=payload.symbol,
        direction=payload.direction,
        confidence=payload.confidence,
        recipients=payload.recipients,
        reasons=payload.reasons,
    )
