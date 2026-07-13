from app.platform_core.clock import utc_now_iso
from app.platform_core.enterprise_scheduler.models import TaskStatus

class TaskStatusRegistry:
    def __init__(self):
        self._statuses: dict[str, TaskStatus] = {}

    def register(self, name: str):
        self._statuses.setdefault(name, TaskStatus(name=name))
        return self._statuses[name]

    def mark_run(self, name: str):
        status = self.register(name)
        status.status = "completed"
        status.run_count += 1
        status.last_run_at = utc_now_iso()
        return status

    def mark_error(self, name: str):
        status = self.register(name)
        status.status = "error"
        status.error_count += 1
        status.last_run_at = utc_now_iso()
        return status

    def list(self):
        return {k: v.__dict__ for k, v in self._statuses.items()}

task_status_registry = TaskStatusRegistry()
