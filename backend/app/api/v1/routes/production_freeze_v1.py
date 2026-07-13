from fastapi import APIRouter
from app.production_freeze_v1.production_freeze_summary import ProductionFreezeSummaryBuilderV1
from app.production_freeze_v1.production_freeze_gate import ProductionFreezeGateBuilderV1
from app.production_freeze_v1.safety_assertions import ProductionSafetyAssertionsBuilderV1

router = APIRouter(prefix="/production-freeze-v1", tags=["production-freeze-v1"])

@router.get("/summary")
async def summary():
    return ProductionFreezeSummaryBuilderV1().build()

@router.get("/gate")
async def gate():
    return ProductionFreezeGateBuilderV1().build()

@router.get("/safety")
async def safety():
    return ProductionSafetyAssertionsBuilderV1().build()
