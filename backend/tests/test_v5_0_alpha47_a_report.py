from app.platform_core.build_pipeline.report import BuildPipelineReportService

def test_report(): assert BuildPipelineReportService().report()['ready'] is True
