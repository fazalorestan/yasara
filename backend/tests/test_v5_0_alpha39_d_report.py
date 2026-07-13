from app.platform_core.live_data_pipeline.cache_report import LiveDataCacheReportService

def test_v500_alpha39_d_report(): assert LiveDataCacheReportService().report()['ready'] is True
