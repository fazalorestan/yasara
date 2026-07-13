class DashboardRefreshContractService:
    def refresh(self):
        return {
            "ready": True,
            "refresh_mode": "on_test_build_run",
            "manual_refresh_supported": True,
            "auto_refresh_supported": True,
            "source": "pic_registries",
            "hardcoded_dashboard": False,
        }

dashboard_refresh_contract_service = DashboardRefreshContractService()
