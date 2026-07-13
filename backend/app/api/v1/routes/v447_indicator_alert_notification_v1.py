from fastapi import APIRouter
from app.v447_indicator_alert_notification.service import IndicatorAlertNotificationFacadeV447

router = APIRouter(prefix="/v4-47/indicator-alert-notification", tags=["v4.47-indicator-alert-notification"])
_service = IndicatorAlertNotificationFacadeV447()

@router.get("/summary")
async def summary():
    return _service.summary()

@router.get("/contract")
async def contract():
    return _service.contract()

@router.get("/sample-alert")
async def sample_alert():
    return _service.sample_alert()

@router.get("/sample-publish")
async def sample_publish():
    return _service.sample_publish()
