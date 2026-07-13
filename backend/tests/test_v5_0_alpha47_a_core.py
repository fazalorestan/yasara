from app.platform_core.build_pipeline.build_core import BuildPipelineCoreService

def test_core(): assert BuildPipelineCoreService().status()['build_enabled'] is True
