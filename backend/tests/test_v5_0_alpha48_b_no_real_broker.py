from app.v500_alpha48_windows_packaging.service import WindowsPackagingFacadeV500Alpha48

def test_no_real_broker(): assert WindowsPackagingFacadeV500Alpha48().report()['real_broker_connection_enabled'] is False
