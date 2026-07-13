from app.v500_alpha50_windows_exe_build.service import WindowsExeBuildScriptFacadeV500Alpha50

def test_no_real_broker(): assert WindowsExeBuildScriptFacadeV500Alpha50().report()['real_broker_connection_enabled'] is False
