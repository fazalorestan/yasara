class DesktopWorkspaceManager:
    def workspace(self):
        return {
            "ready": True,
            "active_workspace": "main",
            "workspaces": ["main", "dashboard", "runtime", "settings"],
            "default_workspace": "dashboard",
            "dashboard_workspace_enabled": True,
            "hardcoded_dashboard": False,
        }

desktop_workspace_manager = DesktopWorkspaceManager()
