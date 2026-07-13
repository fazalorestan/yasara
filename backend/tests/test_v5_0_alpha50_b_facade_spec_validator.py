from app.v500_alpha50_windows_exe_build.service import WindowsExeBuildScriptFacadeV500Alpha50

def test_facade_spec_validator():
 assert WindowsExeBuildScriptFacadeV500Alpha50().spec_validator() is not None
