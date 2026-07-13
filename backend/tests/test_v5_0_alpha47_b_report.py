from app.platform_core.ci_pipeline.report import CIPipelineReportService

def test_report(): assert CIPipelineReportService().report()['ready'] is True
