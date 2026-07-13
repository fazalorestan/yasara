from app.platform_core.project_intelligence.test_summary_view import test_summary_view_service

class DesktopTestStatisticsEngine:
    def statistics(self):
        tests = test_summary_view_service.view()
        return {
            "ready": True,
            "executed": tests["executed"],
            "passed": tests["passed"],
            "failed": tests["failed"],
            "errors": tests["errors"],
            "regression": tests["regression"],
            "source": tests["source"],
            "hardcoded_dashboard": False,
        }

desktop_test_statistics_engine = DesktopTestStatisticsEngine()
