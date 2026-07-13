from app.v500_alpha50_windows_exe_build.service import WindowsExeBuildScriptFacadeV500Alpha50

def test_facade_dist_cleaner():
 assert WindowsExeBuildScriptFacadeV500Alpha50().dist_cleaner() is not None
