from app.v500_alpha50_windows_exe_build.service import WindowsExeBuildScriptFacadeV500Alpha50

def test_dry_run(): assert WindowsExeBuildScriptFacadeV500Alpha50().summary().dry_run is True
