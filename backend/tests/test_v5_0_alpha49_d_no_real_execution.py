from app.v500_alpha49_windows_portable_build.service import WindowsPortableBuildFacadeV500Alpha49

def test_no_real_execution(): assert WindowsPortableBuildFacadeV500Alpha49().report()['real_execution_enabled'] is False
