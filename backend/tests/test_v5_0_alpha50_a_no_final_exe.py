from app.v500_alpha50_windows_real_exe.service import WindowsRealExeBuildPipelineFacadeV500Alpha50

def test_no_final_exe(): assert WindowsRealExeBuildPipelineFacadeV500Alpha50().summary().final_exe_generated is False
