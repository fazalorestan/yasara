from app.platform_core.windows_portable_build.artifact_registration import WindowsPortableArtifactRegistrationContract

def test_artifact(): assert WindowsPortableArtifactRegistrationContract().register()['requires_hash'] is True
