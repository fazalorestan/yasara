from app.platform_core.project_intelligence.dashboard_data_provider import DashboardDataProvider

def test_data(): assert DashboardDataProvider().data()['source']=='pic_registries'
