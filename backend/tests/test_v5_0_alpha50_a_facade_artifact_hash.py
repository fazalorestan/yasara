from app.v500_alpha50_windows_real_exe.service import WindowsRealExeBuildPipelineFacadeV500Alpha50

def test_facade_artifact_hash():
 assert WindowsRealExeBuildPipelineFacadeV500Alpha50().artifact_hash() is not None
