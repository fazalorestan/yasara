from app.platform_core.project_intelligence.dashboard_refresh_contract import DashboardRefreshContractService

def test_refresh(): assert DashboardRefreshContractService().refresh()['auto_refresh_supported'] is True
