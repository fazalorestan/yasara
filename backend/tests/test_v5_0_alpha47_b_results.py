from app.platform_core.ci_pipeline.test_result_registry import TestResultRegistry

def test_results(): assert TestResultRegistry().results()['tests_failed']==0
