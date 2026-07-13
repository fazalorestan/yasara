from app.platform_core.windows_real_exe.artifact_hash import WindowsExeArtifactHashContract

def test_hash(): assert WindowsExeArtifactHashContract().hash_contract()['hash_required'] is True
