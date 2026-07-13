class DesktopWorkspacePanelContract:
    def panel(self):
        return {
            "ready": True,
            "workspace": "main",
            "panels": ["dashboard_panel", "project_panel", "runtime_panel"],
            "active_panel": "dashboard_panel",
            "multi_panel_supported": True,
            "hardcoded_dashboard": False,
        }

desktop_workspace_panel_contract = DesktopWorkspacePanelContract()
