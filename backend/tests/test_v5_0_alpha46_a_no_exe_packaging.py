from app.v500_alpha46_desktop_host.service import DesktopHostFacadeV500Alpha46

def test_no_exe_packaging(): assert DesktopHostFacadeV500Alpha46().summary().exe_packaging_enabled is False
