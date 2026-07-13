from app.platform_core.live_data_pipeline.report import LiveDataPipelineCoreReport

def test_v500_alpha39_a_report_block(): assert LiveDataPipelineCoreReport().report()['execution_allowed'] is False