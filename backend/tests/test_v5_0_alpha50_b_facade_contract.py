from app.v500_alpha50_windows_exe_build.service import WindowsExeBuildScriptFacadeV500Alpha50

def test_facade_contract():
 assert WindowsExeBuildScriptFacadeV500Alpha50().contract() is not None
