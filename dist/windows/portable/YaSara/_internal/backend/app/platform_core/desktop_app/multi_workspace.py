class DesktopMultiWorkspaceService:
    def support(self):
        return {
            "ready": True,
            "multi_workspace_enabled": True,
            "max_workspaces": 8,
            "workspace_switching_enabled": True,
            "persistent_layout": True,
            "hardcoded_dashboard": False,
        }

desktop_multi_workspace_service = DesktopMultiWorkspaceService()
