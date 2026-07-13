from app.v500_alpha46_desktop_foundation.service import DesktopFoundationFacadeV500Alpha46

def test_not_hardcoded(): assert DesktopFoundationFacadeV500Alpha46().contract()["hardcoded_dashboard"] is False
