from app.platform_core.enterprise_scheduler.retry import retry_policy_registry
from app.platform_core.enterprise_scheduler.status import task_status_registry
from app.platform_core.enterprise_scheduler.task_registry import task_registry

class EnterpriseScheduler:
    def seed(self):
        tasks = task_registry.seed_defaults()
        for name in tasks:
            task_status_registry.register(name)
            retry_policy_registry.set_policy(name)
        return {"ready": True, "tasks": tasks, "mode": "report_only"}

    def run_once_report(self, task: str):
        task_registry.seed_defaults()
        if not task_registry.get(task):
            return {"ready": False, "task": task, "error": "task_not_registered"}
        status = task_status_registry.mark_run(task)
        return {"ready": True, "task": task, "status": status.__dict__, "executed": False, "mode": "report_only"}

enterprise_scheduler = EnterpriseScheduler()
