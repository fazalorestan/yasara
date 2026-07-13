from app.v500_alpha50_windows_real_exe.service import WindowsRealExeBuildPipelineFacadeV500Alpha50

def test_no_real_execution(): assert WindowsRealExeBuildPipelineFacadeV500Alpha50().report()['real_execution_enabled'] is False
