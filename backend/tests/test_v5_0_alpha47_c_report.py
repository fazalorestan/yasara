from app.platform_core.release_registry.report import ArtifactReleaseReportService

def test_report(): assert ArtifactReleaseReportService().report()['ready'] is True
