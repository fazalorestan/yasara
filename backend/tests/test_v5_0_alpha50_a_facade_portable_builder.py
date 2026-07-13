from app.v500_alpha50_windows_real_exe.service import WindowsRealExeBuildPipelineFacadeV500Alpha50

def test_facade_portable_builder():
 assert WindowsRealExeBuildPipelineFacadeV500Alpha50().portable_builder() is not None
