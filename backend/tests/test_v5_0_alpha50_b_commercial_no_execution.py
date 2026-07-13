from app.v500_alpha50_windows_exe_build.service import WindowsExeBuildScriptFacadeV500Alpha50

def test_commercial_no_execution(): assert WindowsExeBuildScriptFacadeV500Alpha50().report()['commercial_execution_engine_enabled'] is False
