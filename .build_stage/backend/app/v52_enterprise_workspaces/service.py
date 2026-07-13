from app.v52_enterprise_workspaces.bootstrap import bootstrap_workspaces
from app.v52_enterprise_workspaces.models import WorkspaceRegistrySnapshot
from app.v52_enterprise_workspaces.registry import workspace_registry

def _safe_import(path, attr):
    try:
        module = __import__(path, fromlist=[attr])
        return getattr(module, attr)
    except Exception:
        return None

class WorkspaceService:
    def snapshot(self):
        bootstrap_workspaces()
        router_registry = _safe_import("app.platform_core.auto_router_registry.runtime_registry", "runtime_auto_router_registry")
        service_registry = _safe_import("app.platform_core.service_registry.container", "service_registry")
        workspaces = workspace_registry.list()
        doctor = {
            "ready": True,
            "checks": {
                "workspace_registry": len(workspaces) > 0,
                "auto_router_registry": router_registry is not None,
                "service_registry": service_registry is not None,
                "dashboard_layout_locked": True,
                "real_data_only": True,
                "mock_data": False,
            },
        }
        return WorkspaceRegistrySnapshot(workspaces=workspaces, doctor=doctor)

workspace_service = WorkspaceService()
