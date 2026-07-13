from app.platform_core.project_intelligence.pic_enterprise_report import PICEnterpriseReport, pic_enterprise_report

def test_compat(): assert PICEnterpriseReport().report()['ready'] and pic_enterprise_report.report()['ready']
