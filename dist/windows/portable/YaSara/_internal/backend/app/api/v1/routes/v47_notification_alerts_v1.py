from typing import List

from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter(prefix="/v4-7/notifications", tags=["v4.7-notifications"])


class EventItem(BaseModel):
    id: str
    time: str
    headline: str
    tag: str = "Market"


class NotificationsSummary(BaseModel):
    ready: bool = True
    unread_count: int = 0
    events: List[EventItem] = []


class NotificationChannels(BaseModel):
    ready: bool = True
    channels: List[str] = ["in_app"]


class AlertItem(BaseModel):
    id: str
    time: str
    symbol: str
    detail: str
    severity: str = "low"


class AlertHistory(BaseModel):
    ready: bool = True
    alerts: List[AlertItem] = []


@router.get("/summary", response_model=NotificationsSummary)
async def summary() -> NotificationsSummary:
    return NotificationsSummary()


@router.get("/channels", response_model=NotificationChannels)
async def channels() -> NotificationChannels:
    return NotificationChannels()


@router.get("/alerts", response_model=AlertHistory)
async def alerts() -> AlertHistory:
    return AlertHistory()
