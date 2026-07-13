from app.v500_alpha50_windows_real_exe.service import WindowsRealExeBuildPipelineFacadeV500Alpha50

def test_facade_smoke_test():
 assert WindowsRealExeBuildPipelineFacadeV500Alpha50().smoke_test() is not None
