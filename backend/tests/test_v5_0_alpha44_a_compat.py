from app.platform_core.project_intelligence.pic_report import ProjectIntelligenceReport, project_intelligence_report

def test_compat(): assert ProjectIntelligenceReport().report()['ready'] and project_intelligence_report.report()['ready']
