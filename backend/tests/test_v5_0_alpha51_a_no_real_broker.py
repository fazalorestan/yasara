from app.v500_alpha51_exe_smoke_build.service import WindowsExeSmokeBuildFacadeV500Alpha51

def test_no_real_broker(): assert WindowsExeSmokeBuildFacadeV500Alpha51().report()['real_broker_connection_enabled'] is False
