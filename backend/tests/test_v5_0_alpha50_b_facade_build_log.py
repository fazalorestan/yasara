from app.v500_alpha50_windows_exe_build.service import WindowsExeBuildScriptFacadeV500Alpha50

def test_facade_build_log():
 assert WindowsExeBuildScriptFacadeV500Alpha50().build_log() is not None
