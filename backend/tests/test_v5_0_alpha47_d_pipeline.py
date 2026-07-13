from app.platform_core.build_dashboard.pipeline_status_provider import PipelineStatusProvider

def test_pipeline(): assert PipelineStatusProvider().status()['validation'] is True
