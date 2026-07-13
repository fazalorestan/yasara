from app.platform_core.project_intelligence.test_state import TestStateRegistry

def test_test_state(): assert TestStateRegistry().snapshot()['tests_failed']==0
