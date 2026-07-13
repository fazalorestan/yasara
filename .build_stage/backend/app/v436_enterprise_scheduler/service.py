from app.platform_core.enterprise_scheduler.metrics import task_metrics_reporter
from app.platform_core.enterprise_scheduler.retry import retry_policy_registry
from app.platform_core.enterprise_scheduler.scheduler import enterprise_scheduler
from app.platform_core.enterprise_scheduler.status import task_status_registry
from app.platform_core.enterprise_scheduler.task_registry import task_registry
from app.v436_enterprise_scheduler.models import EnterpriseSchedulerSummaryV436

class EnterpriseSchedulerServiceV436:
    def summary(self):
        return EnterpriseSchedulerSummaryV436()

    def tasks(self):
        return {"ready": True, "tasks": task_registry.seed_defaults()}

    def seed(self):
        return enterprise_scheduler.seed()

    def run_once(self, task: str = "diagnostics_snapshot"):
        return enterprise_scheduler.run_once_report(task)

    def status(self):
        task_registry.seed_defaults()
        return {"ready": True, "status": task_status_registry.list()}

    def retry_policies(self):
        enterprise_scheduler.seed()
        return {"ready": True, "policies": retry_policy_registry.list()}

    def metrics(self):
        enterprise_scheduler.seed()
        return task_metrics_reporter.report()
