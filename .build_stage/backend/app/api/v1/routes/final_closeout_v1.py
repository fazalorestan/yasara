from fastapi import APIRouter
from app.final_closeout_v1.closeout_summary import FinalCloseoutSummaryBuilderV1
from app.final_closeout_v1.actual_test_baseline import ActualTestBaselineBuilderV1
from app.final_closeout_v1.final_zip_instructions import FinalZipInstructionsBuilderV1

router = APIRouter(prefix="/final-closeout-v1", tags=["final-closeout-v1"])

@router.get("/summary")
async def summary():
    return FinalCloseoutSummaryBuilderV1().build()

@router.get("/test-baseline")
async def test_baseline():
    return ActualTestBaselineBuilderV1().build()

@router.get("/zip-instructions")
async def zip_instructions():
    return FinalZipInstructionsBuilderV1().build()
