class DesktopDashboardContractService:
    def contract(self):
        return {
            "ready": True,
            "interface": "desktop_dashboard_contract",
            "methods": ["view_model", "layout", "widgets", "refresh", "report"],
            "runtime_mode": "development_shell",
            "exe_packaging_enabled": False,
            "hardcoded_dashboard": False,
        }

desktop_dashboard_contract_service = DesktopDashboardContractService()
