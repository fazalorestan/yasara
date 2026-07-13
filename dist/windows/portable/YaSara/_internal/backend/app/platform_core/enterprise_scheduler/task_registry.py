from app.platform_core.enterprise_scheduler.models import ScheduledJob

class TaskRegistry:
    def __init__(self):
        self._tasks: dict[str, ScheduledJob] = {}

    def register(self, job: ScheduledJob):
        self._tasks[job.name] = job
        return job

    def get(self, name: str):
        return self._tasks.get(name)

    def list(self):
        return {k: v.__dict__ for k, v in self._tasks.items()}

    def seed_defaults(self):
        if not self._tasks:
            self.register(ScheduledJob(name="diagnostics_snapshot", interval_seconds=300))
            self.register(ScheduledJob(name="plugin_health_check", interval_seconds=120))
            self.register(ScheduledJob(name="release_readiness_check", interval_seconds=600))
        return self.list()

task_registry = TaskRegistry()
