class DesktopDashboardGUIShell:
    def shell(self):
        return {
            "ready": True,
            "build_id": "2026.49.B.001",
            "shell": "desktop_dashboard_gui_shell",
            "default_view": "project_dashboard",
            "live_data_required": True,
            "hardcoded_dashboard_data": False,
            "external_network_required": False,
        }

desktop_dashboard_gui_shell = DesktopDashboardGUIShell()
