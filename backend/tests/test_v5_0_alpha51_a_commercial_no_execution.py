from app.v500_alpha51_exe_smoke_build.service import WindowsExeSmokeBuildFacadeV500Alpha51

def test_commercial_no_execution(): assert WindowsExeSmokeBuildFacadeV500Alpha51().report()['commercial_execution_engine_enabled'] is False
