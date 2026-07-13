from app.platform_core.live_data_pipeline.source_registry import LiveDataSourceRegistry

def test_v500_alpha39_a_source_missing(): assert LiveDataSourceRegistry().get('x')['ready'] is False