from app.platform_core.project_intelligence.desktop_dashboard_contract import DesktopDashboardContractService

def test_contract(): assert DesktopDashboardContractService().contract()['exe_packaging_enabled'] is False
