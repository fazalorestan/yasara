from app.platform_core.desktop_app.dashboard_intelligence_readiness import DesktopDashboardIntelligenceReadinessGate

def test_readiness(): assert DesktopDashboardIntelligenceReadinessGate().run()['ready'] is True
