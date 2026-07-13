from app.platform_core.ai_decision.enterprise.report import AIDecisionSprintReportBuilder

def test_v500_alpha33_d_report_packages(): assert len(AIDecisionSprintReportBuilder().build()['packages']) == 4