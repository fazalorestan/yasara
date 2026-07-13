from app.platform_core.build_dashboard.integration_center import BuildDashboardIntegrationCenter

def test_integration(): assert BuildDashboardIntegrationCenter().dashboard()['source']=='build_ci_release_registries'
