from app.platform_core.project_intelligence.test_state_writer import TestStateWriter

def test_test_writer(): assert TestStateWriter().write_test_state()['tests_failed']==0
