from app.v500_alpha50_windows_exe_build.service import WindowsExeBuildScriptFacadeV500Alpha50

def test_facade_dry_run_executor():
 assert WindowsExeBuildScriptFacadeV500Alpha50().dry_run_executor() is not None
