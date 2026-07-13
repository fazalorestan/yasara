from app.v500_alpha50_windows_exe_build.service import WindowsExeBuildScriptFacadeV500Alpha50

def test_facade_readiness():
 assert WindowsExeBuildScriptFacadeV500Alpha50().readiness() is not None
