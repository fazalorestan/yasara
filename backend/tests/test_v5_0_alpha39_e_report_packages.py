from app.platform_core.live_data_pipeline.enterprise.report import LiveDataEnterpriseReportBuilder

def test_v500_alpha39_e_report_packages(): assert len(LiveDataEnterpriseReportBuilder().build()['packages']) == 5
