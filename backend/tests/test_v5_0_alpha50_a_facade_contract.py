from app.v500_alpha50_windows_real_exe.service import WindowsRealExeBuildPipelineFacadeV500Alpha50

def test_facade_contract():
 assert WindowsRealExeBuildPipelineFacadeV500Alpha50().contract() is not None
