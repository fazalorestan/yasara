from app.v500_alpha46_desktop_foundation.service import DesktopFoundationFacadeV500Alpha46

def test_no_real_execution(): assert DesktopFoundationFacadeV500Alpha46().report()["real_execution_enabled"] is False
