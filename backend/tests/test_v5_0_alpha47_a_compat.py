from app.platform_core.build_pipeline.report import BuildPipelineReport, build_pipeline_report

def test_compat(): assert BuildPipelineReport().report()['ready'] and build_pipeline_report.report()['ready']
