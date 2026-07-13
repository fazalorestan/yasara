from app.v500_alpha50_windows_real_exe.service import WindowsRealExeBuildPipelineFacadeV500Alpha50

def test_facade_readiness():
 assert WindowsRealExeBuildPipelineFacadeV500Alpha50().readiness() is not None
