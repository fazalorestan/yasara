from app.platform_core.project_intelligence.test_state import test_state_registry
class TestSummaryViewService:
    def view(self):
        t = test_state_registry.snapshot()
        return {"ready": True, "executed": t["tests_total"], "passed": t["tests_passed"], "failed": t["tests_failed"], "errors": t["tests_errors"], "regression": t["last_regression_status"], "source": "test_state_registry"}
test_summary_view_service = TestSummaryViewService()
