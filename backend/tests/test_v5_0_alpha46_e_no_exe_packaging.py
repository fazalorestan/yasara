from app.v500_alpha46_desktop_foundation.service import DesktopFoundationFacadeV500Alpha46

def test_no_exe_packaging(): assert DesktopFoundationFacadeV500Alpha46().summary().exe_packaging_enabled is False
