from app.platform_core.project_intelligence.dashboard_readiness import LiveDashboardReadinessGate

def test_readiness(): assert LiveDashboardReadinessGate().run()['ready'] is True
