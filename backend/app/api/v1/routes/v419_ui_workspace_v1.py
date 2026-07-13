from fastapi import APIRouter
from app.v419_ui_workspace.models import UIWorkspacePolishSummaryV419

router = APIRouter(prefix="/v4-19/ui-workspace", tags=["v4.19-ui-workspace"])

@router.get("/summary")
async def summary():
    return UIWorkspacePolishSummaryV419()
