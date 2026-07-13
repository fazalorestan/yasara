from app.v500_alpha49_windows_portable_build.service import WindowsPortableBuildFacadeV500Alpha49

def test_commercial_no_execution(): assert WindowsPortableBuildFacadeV500Alpha49().report()['commercial_execution_engine_enabled'] is False
