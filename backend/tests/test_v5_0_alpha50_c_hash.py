from app.platform_core.windows_packaging_enablement.artifact_hash_plan import WindowsPackagingArtifactHashPlan

def test_hash(): assert WindowsPackagingArtifactHashPlan().plan()['hash_required'] is True
