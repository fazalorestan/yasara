from app.platform_core.project_intelligence.sprint_summary_view import SprintSummaryViewService

def test_sprint(): assert SprintSummaryViewService().view()['current_sprint']=='v5.0-alpha.44'
