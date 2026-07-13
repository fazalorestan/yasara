from app.platform_core.windows_packaging.dashboard_provider import WindowsPackagingDashboardProvider

def test_dashboard(): assert WindowsPackagingDashboardProvider().dashboard()['source']=='windows_packaging_contract'
