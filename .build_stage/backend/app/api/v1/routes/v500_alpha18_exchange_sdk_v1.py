from fastapi import APIRouter
from app.v500_alpha18_exchange_sdk.service import ExchangeSDKFacadeV500Alpha18

router = APIRouter(prefix="/v5-0-alpha-18/exchange-sdk", tags=["v5.0-alpha.18-exchange-sdk"])
_service = ExchangeSDKFacadeV500Alpha18()

@router.get("/summary")
async def summary():
    return _service.summary()

@router.get("/lifecycle")
async def lifecycle():
    return _service.lifecycle()

@router.get("/register")
async def register(exchange_id: str = "binance"):
    return _service.register(exchange_id)

@router.get("/enable")
async def enable(exchange_id: str = "binance"):
    return _service.enable(exchange_id)

@router.get("/connectors")
async def connectors():
    return _service.connectors()

@router.get("/health")
async def health():
    return _service.health()

@router.get("/negotiate")
async def negotiate(exchange_id: str = "binance"):
    return _service.negotiate(exchange_id)

@router.get("/sandbox")
async def sandbox():
    return _service.sandbox()

@router.get("/events")
async def events():
    return _service.events()

@router.get("/readiness")
async def readiness():
    return _service.readiness()
