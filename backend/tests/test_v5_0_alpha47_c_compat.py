from app.platform_core.release_registry.report import ArtifactReleaseReport, artifact_release_report

def test_compat(): assert ArtifactReleaseReport().report()['ready'] and artifact_release_report.report()['ready']
