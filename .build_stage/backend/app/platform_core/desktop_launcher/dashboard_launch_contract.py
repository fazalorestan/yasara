class DashboardLaunchContract:
    def contract(self):
        return {
            "ready": True,
            "dashboard_url": "http://127.0.0.1:8000/api/v1/v5-0-alpha-49/desktop-gui/report",
            "summary_url": "http://127.0.0.1:8000/api/v1/v5-0-alpha-49/desktop-gui/summary",
            "requires_backend_health": True,
            "local_content_only": True,
            "hardcoded_dashboard_data": False,
        }

dashboard_launch_contract = DashboardLaunchContract()
