from app.platform_core.project_intelligence.dashboard_view_model import DashboardViewModelService

def test_view_model(): assert DashboardViewModelService().view_model()['source']=='live_dashboard_backend'
