from app.v500_alpha48_windows_packaging.service import WindowsPackagingFacadeV500Alpha48

def test_no_real_execution(): assert WindowsPackagingFacadeV500Alpha48().report()['real_execution_enabled'] is False
