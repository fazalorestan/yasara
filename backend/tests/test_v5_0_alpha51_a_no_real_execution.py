from app.v500_alpha51_exe_smoke_build.service import WindowsExeSmokeBuildFacadeV500Alpha51

def test_no_real_execution(): assert WindowsExeSmokeBuildFacadeV500Alpha51().report()['real_execution_enabled'] is False
