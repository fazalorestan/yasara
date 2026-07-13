from app.v500_alpha50_windows_real_exe.service import WindowsRealExeBuildPipelineFacadeV500Alpha50

def test_facade_report():
 assert WindowsRealExeBuildPipelineFacadeV500Alpha50().report() is not None
