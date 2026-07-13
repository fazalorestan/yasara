from app.v500_alpha49_windows_portable_build.service import WindowsPortableBuildFacadeV500Alpha49

def test_no_real_broker(): assert WindowsPortableBuildFacadeV500Alpha49().report()['real_broker_connection_enabled'] is False
