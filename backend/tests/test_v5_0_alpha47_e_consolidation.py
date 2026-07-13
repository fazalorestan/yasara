from app.platform_core.production_readiness.consolidation_report import BuildCIReleaseConsolidationReportService

def test_consolidation(): assert BuildCIReleaseConsolidationReportService().report()['consolidated'] is True
