from app.v500_alpha50_windows_real_exe.service import WindowsRealExeBuildPipelineFacadeV500Alpha50

def test_commercial_no_execution(): assert WindowsRealExeBuildPipelineFacadeV500Alpha50().report()['commercial_execution_engine_enabled'] is False
