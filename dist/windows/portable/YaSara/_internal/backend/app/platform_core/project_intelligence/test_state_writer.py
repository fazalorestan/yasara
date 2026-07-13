from app.platform_core.project_intelligence.test_state import test_state_registry
from app.platform_core.project_intelligence.state_store import project_state_store

class TestStateWriter:
    def write_test_state(self):
        tests = test_state_registry.snapshot()
        return {
            "ready": True,
            "written": True,
            "tests_total": tests["tests_total"],
            "tests_passed": tests["tests_passed"],
            "tests_failed": tests["tests_failed"],
            "tests_errors": tests["tests_errors"],
            "regression": tests["last_regression_status"],
            "store": project_state_store.base_state()["source"],
        }

test_state_writer = TestStateWriter()
