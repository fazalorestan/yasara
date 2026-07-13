from app.platform_core.ci_pipeline.report import CIPipelineReport, ci_pipeline_report

def test_compat(): assert CIPipelineReport().report()['ready'] and ci_pipeline_report.report()['ready']
