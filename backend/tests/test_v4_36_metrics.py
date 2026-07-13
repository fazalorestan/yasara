from app.platform_core.enterprise_scheduler.metrics import TaskMetricsReporter
from app.platform_core.enterprise_scheduler.status import task_status_registry

def test_v436_metrics():
    task_status_registry.mark_run("metric_test")
    r = TaskMetricsReporter().report()
    assert r["ready"] is True
    assert r["total_runs"] >= 1
