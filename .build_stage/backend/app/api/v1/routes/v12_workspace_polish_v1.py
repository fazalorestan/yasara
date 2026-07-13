from fastapi import APIRouter
from app.v12_workspace_polish.service import WorkspacePolishServiceV12
router = APIRouter(prefix="/v1-2/workspace-polish", tags=["v1.2-workspace-polish"])
@router.get("/summary")
async def summary():
    return WorkspacePolishServiceV12().summary()
