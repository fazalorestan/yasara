from app.platform_core.build_pipeline.build_dashboard_provider import BuildDashboardProvider

def test_dashboard(): assert BuildDashboardProvider().dashboard()['source']=='build_pipeline_registries'
