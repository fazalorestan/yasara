from app.platform_core.project_intelligence.pic_enterprise_report import PICEnterpriseReportService

def test_report(): assert PICEnterpriseReportService().report()['hardcoded_dashboard'] is False
