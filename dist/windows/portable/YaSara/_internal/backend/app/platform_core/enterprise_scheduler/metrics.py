from app.platform_core.enterprise_scheduler.status import task_status_registry

class TaskMetricsReporter:
    def report(self):
        statuses = task_status_registry.list()
        total_runs = sum(v.get("run_count", 0) for v in statuses.values())
        total_errors = sum(v.get("error_count", 0) for v in statuses.values())
        return {
            "ready": True,
            "task_count": len(statuses),
            "total_runs": total_runs,
            "total_errors": total_errors,
            "mode": "report_only",
        }

task_metrics_reporter = TaskMetricsReporter()
