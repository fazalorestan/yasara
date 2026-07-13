from fastapi import APIRouter
from app.final_delivery_pack_v1.delivery_pack_summary import DeliveryPackSummaryBuilderV1
from app.final_delivery_pack_v1.delivery_readme import DeliveryReadmeBuilderV1
from app.final_delivery_pack_v1.final_commands import FinalCommandsBuilderV1
from app.final_delivery_pack_v1.final_project_card import FinalProjectCardBuilderV1

router = APIRouter(prefix="/final-delivery-pack-v1", tags=["final-delivery-pack-v1"])

@router.get("/summary")
async def summary():
    return DeliveryPackSummaryBuilderV1().build()

@router.get("/project-card")
async def project_card():
    return FinalProjectCardBuilderV1().build()

@router.get("/commands")
async def commands():
    return FinalCommandsBuilderV1().build()

@router.get("/readme")
async def readme():
    return DeliveryReadmeBuilderV1().build()
