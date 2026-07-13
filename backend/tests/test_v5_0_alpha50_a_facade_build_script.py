from app.v500_alpha50_windows_real_exe.service import WindowsRealExeBuildPipelineFacadeV500Alpha50

def test_facade_build_script():
 assert WindowsRealExeBuildPipelineFacadeV500Alpha50().build_script() is not None
