from fastapi import APIRouter
from app.v423_plugin_catalog.service import PluginCatalogServiceV423

router = APIRouter(prefix="/v4-23/plugin-catalog", tags=["v4.23-plugin-catalog"])
_service = PluginCatalogServiceV423()

@router.get("/summary")
async def summary():
    return _service.summary()

@router.get("/catalog")
async def catalog():
    return _service.catalog()

@router.get("/evaluate")
async def evaluate():
    return _service.evaluate()
