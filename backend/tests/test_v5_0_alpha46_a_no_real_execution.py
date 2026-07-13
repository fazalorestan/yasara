from app.v500_alpha46_desktop_host.service import DesktopHostFacadeV500Alpha46

def test_no_real_execution(): assert DesktopHostFacadeV500Alpha46().report()['real_execution_enabled'] is False
