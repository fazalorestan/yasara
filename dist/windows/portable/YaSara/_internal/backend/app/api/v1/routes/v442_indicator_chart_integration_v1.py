from fastapi import APIRouter
from app.v442_indicator_chart_integration.service import IndicatorChartIntegrationServiceV442

router = APIRouter(prefix="/v4-42/indicator-chart-integration", tags=["v4.42-indicator-chart-integration"])
_service = IndicatorChartIntegrationServiceV442()

@router.get("/summary")
async def summary():
    return _service.summary()

@router.get("/chart-binding")
async def chart_binding():
    return _service.chart_binding()

@router.get("/visibility")
async def visibility():
    return _service.visibility()

@router.get("/update-contract")
async def update_contract():
    return _service.update_contract()
