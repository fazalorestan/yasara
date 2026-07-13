from app.platform_core.release_candidate.report import InternalRCPreparationReportService

def test_report(): assert InternalRCPreparationReportService().report()['ready'] is True
