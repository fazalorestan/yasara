from app.platform_core.build_dashboard.readiness import BuildDashboardIntegrationReadinessGate

def test_readiness(): assert BuildDashboardIntegrationReadinessGate().run()['ready'] is True
