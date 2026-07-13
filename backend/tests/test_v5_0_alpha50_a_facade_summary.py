from app.v500_alpha50_windows_real_exe.service import WindowsRealExeBuildPipelineFacadeV500Alpha50

def test_facade_summary():
 assert WindowsRealExeBuildPipelineFacadeV500Alpha50().summary() is not None
