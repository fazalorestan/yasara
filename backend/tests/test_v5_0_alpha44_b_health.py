from app.platform_core.project_intelligence.health_summary_view import HealthSummaryViewService

def test_health(): assert HealthSummaryViewService().view()['project_health']=='green'
