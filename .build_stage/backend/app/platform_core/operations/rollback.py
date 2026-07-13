class RollbackPlan:
    def plan(self):
        return {
            "ready": True,
            "steps": ["stop_runtime", "restore_latest_backup", "run_tests", "run_diagnostics", "start_runtime", "validate_dashboard"],
            "destructive": False,
            "mode": "plan_only",
        }

rollback_plan = RollbackPlan()
