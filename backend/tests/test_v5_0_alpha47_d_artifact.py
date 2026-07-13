from app.platform_core.build_dashboard.artifact_signal_provider import ArtifactSignalProvider

def test_artifact(): assert ArtifactSignalProvider().signal()['signal']=='green'
