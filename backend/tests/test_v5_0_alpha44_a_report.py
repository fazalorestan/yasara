from app.platform_core.project_intelligence.pic_report import ProjectIntelligenceReportService

def test_report(): assert ProjectIntelligenceReportService().report()['hardcoded_dashboard'] is False
