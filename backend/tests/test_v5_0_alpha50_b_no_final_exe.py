from app.v500_alpha50_windows_exe_build.service import WindowsExeBuildScriptFacadeV500Alpha50

def test_no_final_exe(): assert WindowsExeBuildScriptFacadeV500Alpha50().summary().final_exe_generated is False
