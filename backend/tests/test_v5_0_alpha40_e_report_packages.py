from app.platform_core.ai_intelligence.enterprise.report import AIEnterpriseReportBuilder

def test_v500_alpha40_e_report_packages(): assert len(AIEnterpriseReportBuilder().build()['packages']) == 5
