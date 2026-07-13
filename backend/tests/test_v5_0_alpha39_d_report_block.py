from app.platform_core.live_data_pipeline.cache_report import LiveDataCacheReportService

def test_v500_alpha39_d_report_block(): assert LiveDataCacheReportService().report()['execution_allowed'] is False
