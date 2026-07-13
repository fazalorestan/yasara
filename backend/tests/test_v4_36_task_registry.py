from app.platform_core.enterprise_scheduler.task_registry import TaskRegistry

def test_v436_task_registry():
    r = TaskRegistry()
    tasks = r.seed_defaults()
    assert "diagnostics_snapshot" in tasks
