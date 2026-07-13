from app.platform_core.project_intelligence.state_sync_report import state_sync_report_service

class StateSyncReadinessGate:
    def run(self):
        report = state_sync_report_service.report()
        ready = (
            report["ready"]
            and report["build_write"]["written"]
            and report["test_write"]["written"]
            and report["sprint_write"]["written"]
            and report["dashboard_auto_update_ready"]
        )
        return {
            "ready": ready,
            "checks": {
                "store_ready": report["store"]["ready"],
                "build_state_written": report["build_write"]["written"],
                "test_state_written": report["test_write"]["written"],
                "sprint_state_written": report["sprint_write"]["written"],
                "dashboard_auto_update_ready": report["dashboard_auto_update_ready"],
                "hardcoded_dashboard": False,
            },
        }

state_sync_readiness_gate = StateSyncReadinessGate()
