from app.release_pro_v1.build_pipeline import BuildPipelineBuilderV1

def test_build_pipeline_has_tests():
    pipeline = BuildPipelineBuilderV1().windows_release()
    assert any(step.name == "run_tests" for step in pipeline.steps)
