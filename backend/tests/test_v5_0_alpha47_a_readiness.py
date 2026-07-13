from app.platform_core.build_pipeline.readiness import BuildPipelineReadinessGate

def test_readiness(): assert BuildPipelineReadinessGate().run()['ready'] is True
