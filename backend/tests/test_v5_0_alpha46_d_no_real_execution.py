from app.v500_alpha46_desktop_dashboard_intelligence.service import DesktopDashboardIntelligenceFacadeV500Alpha46

def test_no_real_execution(): assert DesktopDashboardIntelligenceFacadeV500Alpha46().report()['real_execution_enabled'] is False
