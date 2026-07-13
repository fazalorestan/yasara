from app.v500_alpha50_windows_exe_build.service import WindowsExeBuildScriptFacadeV500Alpha50

def test_facade_command_builder():
 assert WindowsExeBuildScriptFacadeV500Alpha50().command_builder() is not None
