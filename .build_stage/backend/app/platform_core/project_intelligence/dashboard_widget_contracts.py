class DashboardWidgetContractService:
    def widgets(self):
        return {
            "ready": True,
            "widgets": [
                {"id": "project_progress", "type": "progress"},
                {"id": "windows_progress", "type": "progress"},
                {"id": "android_progress", "type": "progress"},
                {"id": "ios_progress", "type": "progress"},
                {"id": "web_progress", "type": "progress"},
                {"id": "tests", "type": "summary"},
                {"id": "modules", "type": "list"},
                {"id": "health", "type": "status"},
            ],
            "count": 8,
            "hardcoded_dashboard": False,
        }

dashboard_widget_contract_service = DashboardWidgetContractService()
