from app.platform_core.project_intelligence.test_summary_view import TestSummaryViewService

def test_tests(): assert TestSummaryViewService().view()['failed']==0
