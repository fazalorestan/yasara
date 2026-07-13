from app.platform_core.windows_exe_build.artifact_plan import WindowsExeArtifactPlan

def test_artifact(): assert WindowsExeArtifactPlan().plan()['hash_created'] is False
