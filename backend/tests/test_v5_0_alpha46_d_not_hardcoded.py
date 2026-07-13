from app.v500_alpha46_desktop_dashboard_intelligence.service import DesktopDashboardIntelligenceFacadeV500Alpha46

def test_not_hardcoded(): assert DesktopDashboardIntelligenceFacadeV500Alpha46().contract()['hardcoded_dashboard'] is False
