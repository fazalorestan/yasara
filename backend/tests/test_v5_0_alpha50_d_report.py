from app.platform_core.windows_artifact_registration.report import LocalExeArtifactRegistrationReportService

def test_report(): assert LocalExeArtifactRegistrationReportService().report()['ready'] is True
