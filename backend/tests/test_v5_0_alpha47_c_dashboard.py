from app.platform_core.release_registry.release_dashboard_provider import ReleaseDashboardProvider

def test_dashboard(): assert ReleaseDashboardProvider().dashboard()['source']=='release_registry'
