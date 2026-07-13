from app.platform_core.ci_pipeline.readiness import CIPipelineReadinessGate

def test_readiness(): assert CIPipelineReadinessGate().run()['ready'] is True
