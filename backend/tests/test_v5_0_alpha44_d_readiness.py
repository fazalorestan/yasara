from app.platform_core.project_intelligence.desktop_dashboard_readiness import DesktopDashboardReadinessGate

def test_readiness(): assert DesktopDashboardReadinessGate().run()['ready'] is True
