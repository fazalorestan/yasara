from fastapi import APIRouter
from app.v500_alpha16_exchange_connector.service import ExchangeConnectorFacadeV500Alpha16

router = APIRouter(prefix="/v5-0-alpha-16/exchange-connector", tags=["v5.0-alpha.16-exchange-connector"])
_service = ExchangeConnectorFacadeV500Alpha16()

@router.get("/summary")
async def summary():
    return _service.summary()

@router.get("/list")
async def list_exchanges():
    return _service.list()

@router.get("/exchange")
async def exchange(exchange_id: str = "binance"):
    return _service.exchange(exchange_id)

@router.get("/capabilities")
async def capabilities(exchange_id: str | None = None):
    return _service.capabilities(exchange_id)

@router.get("/metadata")
async def metadata(exchange_id: str | None = None):
    return _service.metadata(exchange_id)

@router.get("/health")
async def health():
    return _service.health()

@router.get("/connector-contract")
async def connector_contract():
    return _service.connector_contract()

@router.get("/readiness")
async def readiness():
    return _service.readiness()
