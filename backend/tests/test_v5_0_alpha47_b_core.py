from app.platform_core.ci_pipeline.ci_core import CIPipelineCoreService

def test_core(): assert CIPipelineCoreService().status()['ci_enabled'] is True
