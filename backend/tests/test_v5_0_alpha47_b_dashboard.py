from app.platform_core.ci_pipeline.ci_dashboard_provider import CIDashboardProvider

def test_dashboard(): assert CIDashboardProvider().dashboard()['source']=='ci_pipeline_registries'
