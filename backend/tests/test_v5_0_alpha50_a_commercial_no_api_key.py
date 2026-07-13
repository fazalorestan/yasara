from app.v500_alpha50_windows_real_exe.service import WindowsRealExeBuildPipelineFacadeV500Alpha50

def test_commercial_no_api_key(): assert WindowsRealExeBuildPipelineFacadeV500Alpha50().report()['commercial_api_key_required'] is False
