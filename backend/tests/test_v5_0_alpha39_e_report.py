from app.platform_core.live_data_pipeline.enterprise.report import LiveDataEnterpriseReportBuilder

def test_v500_alpha39_e_report(): assert LiveDataEnterpriseReportBuilder().build()['ready'] is True
