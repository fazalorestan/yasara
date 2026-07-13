from app.v500_alpha50_windows_exe_build.service import WindowsExeBuildScriptFacadeV500Alpha50

def test_facade_artifact_plan():
 assert WindowsExeBuildScriptFacadeV500Alpha50().artifact_plan() is not None
