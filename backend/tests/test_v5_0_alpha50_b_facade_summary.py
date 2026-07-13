from app.v500_alpha50_windows_exe_build.service import WindowsExeBuildScriptFacadeV500Alpha50

def test_facade_summary():
 assert WindowsExeBuildScriptFacadeV500Alpha50().summary() is not None
