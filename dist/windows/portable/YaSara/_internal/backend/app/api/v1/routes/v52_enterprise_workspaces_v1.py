from fastapi import APIRouter, HTTPException
from app.v52_enterprise_workspaces.registry import workspace_registry
from app.v52_enterprise_workspaces.service import workspace_service

router = APIRouter(prefix="/enterprise/workspaces", tags=["enterprise-workspaces"])

@router.get("")
async def list_workspaces():
    return workspace_service.snapshot()

@router.get("/{workspace_id}")
async def get_workspace(workspace_id: str):
    item = workspace_registry.get(workspace_id)
    if item is None:
        raise HTTPException(status_code=404, detail="workspace_not_found")
    return item

@router.get("/doctor/health")
async def doctor():
    return workspace_service.snapshot().doctor

@router.get("/contract/stability")
async def stability_contract():
    return {
        "build_id": "2026.46.ENTERPRISE.001",
        "real_backend_data_only": True,
        "mock_data": False,
        "dashboard_layout_locked": True,
        "root_app_unchanged": True,
        "signal_only_default": True,
        "auto_trading_enabled": False,
    }
